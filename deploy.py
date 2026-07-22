#!/usr/bin/env python3
"""deploy.py - one-command release for Hyrox-Prep.

Usage:
  python3 deploy.py "commit message"    # bump + validate + commit + push + poll live
  python3 deploy.py --check             # bump + validate only, no git (prints next version)

What it does:
  1. Reads VERSION (index.html), BUILD (index.html), hyrox-vNN (sw.js); ABORTS if out of sync.
  2. Bumps all three by +1 IN MEMORY.
  3. Syntax-checks the extracted <script> + sw.js via JavaScriptCore (node is not installed here)
     BEFORE writing to disk, so a syntax error never ships a half-bumped file.
  4. Sanity-checks the workouts array (entry count).
  5. Writes files, commits ALL changes (git add -A), pushes to main, polls the live GitHub
     Pages URL until the new VERSION appears.

NOTE: this does NOT run a browser render check. Per CLAUDE.md, changes that touch app LOGIC,
rendering, or structure still need a manual browser preview FIRST. This script is for the
mechanical release + syntax/version safety, which fully covers content-only edits
(weights / sets / cues / benchmark tables).
"""
import sys, re, os, time, tempfile, subprocess, urllib.request, random

LIVE = "https://choonang-lab.github.io/Hyrox-Prep/index.html"

def die(m): sys.exit("ABORT: " + m)

def jsc_check(paths):
    jxa = ('function run(){ObjC.import("Foundation");'
           'function r(p){return $.NSString.stringWithContentsOfFileEncodingError(p,$.NSUTF8StringEncoding,null).js;}'
           'var o=[];PATHS.forEach(function(f){try{new Function(r(f));o.push("OK   "+f);}catch(e){o.push("FAIL "+f+"  ::  "+e.message);}});return o.join("\\n");}')
    jxa = jxa.replace("PATHS", "[" + ",".join('"%s"' % p for p in paths) + "]")
    f = tempfile.NamedTemporaryFile("w", suffix=".js", delete=False); f.write(jxa); f.close()
    res = subprocess.run(["osascript", "-l", "JavaScript", f.name], capture_output=True, text=True)
    os.unlink(f.name)
    return res.stdout.strip()

def main():
    args = sys.argv[1:]
    check_only = "--check" in args
    msg = next((a for a in args if not a.startswith("--")), None)
    if not check_only and not msg:
        die('usage: python3 deploy.py "commit message"   (or --check)')

    html = open("index.html").read()
    sw = open("sw.js").read()
    mv = re.search(r"VERSION (\d+)</div>", html)
    mb = re.search(r"BUILD (\d+)</strong>", html)
    ms = re.search(r"hyrox-v(\d+)", sw)
    if not (mv and mb and ms): die("could not locate all three version markers")
    cur = int(mv.group(1))
    if not (int(mb.group(1)) == cur == int(ms.group(1))):
        die("version triplet OUT OF SYNC: VERSION=%s BUILD=%s sw=%s" % (mv.group(1), mb.group(1), ms.group(1)))
    nxt = cur + 1

    html2 = html.replace("VERSION %d</div>" % cur, "VERSION %d</div>" % nxt, 1) \
                .replace("BUILD %d</strong>" % cur, "BUILD %d</strong>" % nxt, 1)
    sw2 = sw.replace("hyrox-v%d" % cur, "hyrox-v%d" % nxt, 1)
    if not ("VERSION %d</div>" % nxt in html2 and "BUILD %d</strong>" % nxt in html2 and "hyrox-v%d" % nxt in sw2):
        die("post-bump sync failed")

    # syntax check on the bumped content BEFORE writing
    scripts = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", html2, re.S)
    tmp_app = tempfile.NamedTemporaryFile("w", suffix=".js", delete=False)
    tmp_app.write("\n;\n".join(scripts)); tmp_app.close()
    tmp_sw = tempfile.NamedTemporaryFile("w", suffix=".js", delete=False)
    tmp_sw.write(sw2); tmp_sw.close()
    out = jsc_check([tmp_app.name, tmp_sw.name])
    os.unlink(tmp_app.name); os.unlink(tmp_sw.name)
    print(out)
    if "FAIL" in out:
        die("syntax check failed - files NOT written, nothing committed")

    n = html2.count("{id:uid(),week:")
    print("plan entries: %d" % n)
    if n < 400:
        die("workouts array looks truncated (%d entries) - not writing" % n)

    print("validated  v%d -> v%d" % (cur, nxt))
    if check_only:
        print("--check only: no files written, no git actions.")
        return

    open("index.html", "w").write(html2)
    open("sw.js", "w").write(sw2)

    subprocess.run(["git", "add", "-A"], check=True)
    cm = subprocess.run(["git", "commit", "-m", msg], capture_output=True, text=True)
    if cm.returncode != 0:
        print(cm.stdout, cm.stderr); die("git commit failed")
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("committed + pushed  v%d" % nxt)

    print("polling live for VERSION %d ..." % nxt)
    target = "VERSION %d" % nxt
    for i in range(12):
        try:
            with urllib.request.urlopen(LIVE + "?cb=%d%d" % (random.randint(0, 999999), i), timeout=15) as r:
                body = r.read().decode("utf-8", "ignore")
            if target in body:
                print("LIVE = v%d" % nxt); return
        except Exception as e:
            print("  poll %d: %s" % (i + 1, e))
        time.sleep(20)
    print("NOTE: v%d pushed but not yet visible after polling - Pages may be building; check manually." % nxt)

if __name__ == "__main__":
    main()

:: USAGE: build <commit message for gh-pages branch>

pelican content/ -o output/ -s publishconf.py

if not "%1" == "" (ghp-import -m "%~1" output)
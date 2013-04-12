:: USAGE: build <commit message for gh-pages branch>

pelican content/ -o output/ -s publishconf.py

ghp-import -m "%1" output
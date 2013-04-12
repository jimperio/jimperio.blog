:: USAGE: build <commit message for gh-pages branch>

pelican content/ -o output/ -s publishconf.py

python ghp-import -m "%1" output
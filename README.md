# jimperio.blog

## ABOUT
The source for my current blog.

Uses Pelican to generate the static output.


## NOTES:
Pelican 3.1.1 is the latest package, but it does not yet include support for the override attributes 'url' and 'save_as', so just install the latest from source (https://github.com/getpelican/pelican) for now.

There's a weird issue with locale.getlocale() on OS X, and having an invalid encoding returned causes some issues with Pelican. A quick fix is to just set the LANG environment variable to, say, "en_US.UTF-8".


## TODO:
A whole lot. But it works for now, so just get writing, you!

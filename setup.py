from setuptools import setup

def main():
  setup(name='jimperio.blog',
        version='0.9.2',
        install_requires=[
          'pelican==3.5.0',
          'Markdown',
          # See NOTES.txt. Use the included submodule.
          #'ghp-import',
        ],)

if __name__ == "__main__":
  main()

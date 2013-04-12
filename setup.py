from setuptools import setup

def main():
  setup(name='jimperio.blog',
        version='0.9.0',
        install_requires=[
        									# See NOTES.txt regarding pelican and ghp-import.
			                    #'pelican >= 3.1.1',
                          'Markdown',
                          #'ghp-import',
                         ],)

if __name__ == "__main__":
  main()

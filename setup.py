from distutils.core import setup

files = ["voids_cribe/data/*", "voids_cribe/data/Names/*", "voids_cribe/data/MarkovDictionaries/*"]

setup(name = "void_scribe",
    version = "0.1a",
    description = "Procedural Natural Language Generation",
    author = "Stephen Brasel, Joshua Myers",
    packages = ['void_scribe'],
    package_dir = {'void_scribe':'void_scribe'},
    include_package_data=True,
    install_requires=[
          'nlglib',
          'pickle',
          'random',
          'os',
          'requests',
          'pkg_resources'
      ]
) 
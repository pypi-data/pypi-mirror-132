from setuptools import setup

name = "types-pyaudio"
description = "Typing stubs for pyaudio"
long_description = '''
## Typing stubs for pyaudio

This is a PEP 561 type stub package for the `pyaudio` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `pyaudio`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/pyaudio. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `14e5d16c3a2de82548ea583b525869c6d2b43d42`.
'''.lstrip()

setup(name=name,
      version="0.2.6",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires=[],
      packages=['pyaudio-stubs'],
      package_data={'pyaudio-stubs': ['__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Typed",
      ]
)

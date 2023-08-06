from setuptools import setup

name = "types-decorator"
description = "Typing stubs for decorator"
long_description = '''
## Typing stubs for decorator

This is a PEP 561 type stub package for the `decorator` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `decorator`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/decorator. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `22bf9e8a787b38b1a0e193edd5b47119e43286ca`.
'''.lstrip()

setup(name=name,
      version="5.1.1",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires=[],
      packages=['decorator-stubs'],
      package_data={'decorator-stubs': ['__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Typed",
      ]
)

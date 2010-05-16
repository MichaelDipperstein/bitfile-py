from distutils.core import setup

__desc__  = """
=============
BitFile Class
=============
Description
-----------
This archive contains a python package that includes a class implementing
bitwise reading and writing for sequential files.  This class is intended to be
easy to follow and expand upon, though it may be used without an understanding
of its implementation.

License
-------
BitFile is licensed under the GNU General Public License v3.  See COPYING for
full license text.

Files
-----
::

    __init__.py     - Python package initializtion code for bitfile.
    bitfile.py      - Class implementing bitwise reading and writing for
    sequential files.
    COPYING         - GNU General Public License v3
    README          - Package documentation
    sample.py       - Sample usage and doctest.
    setup.py        - distutils setup file.

Installing
----------
This package uses distutils.  The package may be installed with the following
command::

    python setup.py install

Usage
-----
bitfile.py is fully documented with docstrings.  Use your favorite tool for
generating documentation from docstrings.

sample.py demonstrates usage of each of the BitFile methods.

sample.py also contains doctest information.  The doctest may be excuted with
the following command::

    python sample.py -v

History
-------
| 01/14/10 - Initial release
| 03/04/10 - Add support for 'r+' (read/write) mode

ToDo
----
* Add constructor to convert a standard file into a BitFile.
"""

__classifiers__ = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: System :: Archiving :: Compression',
    'Topic :: Utilities',
]

setup(name='bitfile',
      version='0.2',
      description=\
        'Module for reading/writing an arbitrary number of bits from a file.',
      author='Michael Dipperstein',
      author_email='mdipper@alumni.engr.ucsb.edu',
      license='GPL',
      url='http://michael.dipperstein.com/bitlibs/',
      packages=['bitfile',],
      package_data={'bitfile': ['COPYING', 'README']},
      platforms='All platforms',
      long_description=__desc__,
      classifiers=__classifiers__,
     )

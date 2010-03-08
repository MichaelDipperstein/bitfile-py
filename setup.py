from distutils.core import setup

setup(name='bitfile',
      version='0.1',
      description=\
        'Module for reading/writing an arbitrary number of bits from a file.',
      author='Michael Dipperstein',
      author_email='mdipper@alumni.engr.ucsb.edu',
      license='GPL',
      url='http://michael.dipperstein.com/bitlibs/',
      packages=['bitfile',],
      package_data={'bitfile': ['COPYING', 'README']},
      platforms='All platforms',
      long_description="""A simple class of I/O methods for files that contain
        data in sizes that aren't integral bytes.  The methods contained in
        this class were created with compression algorithms in mind, but may
        be suited to other applications."""
     )

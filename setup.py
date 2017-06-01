from tables3 import __version__

from setuptools import setup

try:
    from testr.setup_helper import cmdclass
except ImportError:
    cmdclass = {}

setup(name='tables3',
      author='Jean Connelly, Tom Aldcroft',
      description='pytables 2 to 3 compatibility methods',
      author_email='jconnelly@cfa.harvard.edu',
      version=__version__,
      zip_safe=False,
      packages=['tables3', 'tables3.tests'],
      tests_require=['pytest'],
      cmdclass=cmdclass,
      )

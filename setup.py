# Licensed under a 3-clause BSD style license - see LICENSE.rst
from setuptools import setup

try:
    from testr.setup_helper import cmdclass
except ImportError:
    cmdclass = {}

setup(name='tables3_api',
      author='Jean Connelly, Tom Aldcroft',
      description='pytables 2 to 3 compatibility methods',
      author_email='jconnelly@cfa.harvard.edu',
      use_scm_version=True,
      setup_requires=['setuptools_scm', 'setuptools_scm_git_archive'],
      zip_safe=False,
      packages=['tables3_api', 'tables3_api.tests'],
      tests_require=['pytest'],
      cmdclass=cmdclass,
      )

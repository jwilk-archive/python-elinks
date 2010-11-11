'''
python-elinks installs an encoding error handler that uses the same ASCII replacements as ELinks does.
'''

classifiers = '''
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: GNU General Public License (GPL)
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 3
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Text Processing :: Filters
'''.strip().split('\n')

import os
import distutils.core

try:
    # Python 3.X
    from distutils.command.build_py import build_py_2to3 as distutils_build_py
except ImportError:
    # Python 2.X
    from distutils.command.build_py import build_py as distutils_build_py

os.putenv('TAR_OPTIONS', '--owner root --group root --mode a+rX')

distutils.core.setup(
    name = 'python-elinks',
    version = '0.2',
    license = 'GNU GPL 2',
    platforms = ['any'],
    description = 'ELinks-like encoding error handler',
    long_description = __doc__.strip(),
    classifiers = classifiers,
    url = 'http://jwilk.net/software/python-elinks',
    author = 'Jakub Wilk',
    author_email = 'jwilk@jwilk.net',
    packages = ['elinks'],
    cmdclass = dict(build_py=distutils_build_py),
)

# vim:ts=4 sw=4 et

'''
python-elinks installs an encoding error handler that uses the same ASCII replacements as ELinks does.
'''

classifiers = '''\
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: GNU General Public License (GPL)
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Text Processing :: Filters'''.split('\n')

import os
import distutils.core

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
    packages = ['elinks']
)

# vim:ts=4 sw=4 et

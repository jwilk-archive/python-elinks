'''
python-elinks installs an encoding error handler that uses the same ASCII replacements as ELinks does.
'''

classifiers = '''\
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Text Processing :: Filters'''.split('\n')

from distutils.core import setup

setup(
    name = 'python-elinks',
    version = '0.2',
    license = 'MIT',
    platforms = ['any'],
    description = 'ELinks-like encoding error handler',
    long_description = __doc__.strip(),
    classifiers = classifiers,
    url = 'http://python-elinks.googlecode.com/',
    author = 'Jakub Wilk',
    author_email = 'jwilk@jwilk.net',
    packages = ['elinks']
)

# vim:ts=4 sw=4 et

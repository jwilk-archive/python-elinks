# encoding=UTF-8

# Copyright © 2007-2015 Jakub Wilk <jwilk@jwilk.net>
#
# This file is part of python-elinks.
#
# python-elinks is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published
# by the Free Software Foundation.
#
# python-elinks is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.

'''
python-elinks installs an encoding error handler that uses the same ASCII replacements as ELinks does.
'''

import io

import distutils.core

try:
    # Python 3.X
    from distutils.command.build_py import build_py_2to3 as distutils_build_py
except ImportError:
    # Python 2.X
    from distutils.command.build_py import build_py as distutils_build_py

try:
    import distutils644
except ImportError:
    pass
else:
    distutils644.install()

b''  # Python >= 2.6 is required

def get_version():
    d = {}
    with io.open('elinks/__init__.py', encoding='UTF-8') as file:
        for line in file:
            if line.startswith('__version__ ='):
                exec(line, d)
                break
    return d['__version__']

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
'''.strip().splitlines()

distutils.core.setup(
    name='python-elinks',
    version=get_version(),
    license='GNU GPL 2',
    description='ELinks-like encoding error handler',
    long_description=__doc__.strip(),
    classifiers=classifiers,
    url='http://jwilk.net/software/python-elinks',
    author='Jakub Wilk',
    author_email='jwilk@jwilk.net',
    packages=['elinks'],
    cmdclass=dict(build_py=distutils_build_py),
)

# vim:ts=4 sts=4 sw=4 et

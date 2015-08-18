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

'''Register the elinks-like encoding error handler.'''

__author__ = 'Jakub Wilk <jwilk@jwilk.net>'
__version__ = '0.3'

from elinks.mapping import MAPPING
from codecs import register_error as _register_error

def handler(exception):
    '''The elinks-like encoding error handler.'''
    if isinstance(exception, (UnicodeEncodeError, UnicodeTranslateError)):
        return ''.join(MAPPING.get(ch, u'*') for ch in exception.object[exception.start:exception.end]), exception.end
    else:
        raise TypeError("Don't know how to handle {exc} in error callback".format(exc=type(exception).__name__))

_register_error('elinks', handler)

# vim:ts=4 sts=4 sw=4 et

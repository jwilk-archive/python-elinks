# encoding=UTF-8

# Copyright © 2007, 2010 Jakub Wilk <jwilk@jwilk.net>
#
# This package is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.

'''Register the elinks-like encoding error handler.'''

__author__ = 'Jakub Wilk <jwilk@jwilk.net>'
__version__ = '0.2'

from elinks.mapping import MAPPING
from codecs import register_error as _register_error

def handler(exception):
    '''The elinks-like encoding error handler.'''
    if isinstance(exception, (UnicodeEncodeError, UnicodeTranslateError)):
        return ''.join(MAPPING.get(ch, u'*') for ch in exception.object[exception.start:exception.end]), exception.end
    else:
        raise TypeError("Don't know how to handle %s in error callback" % exception.__class__.__name__)

_register_error('elinks', handler)

# vim:ts=4 sw=4 et

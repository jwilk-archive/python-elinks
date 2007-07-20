'''Register the elinks-like encoding error handler.'''

__author__ = 'Jakub Wilk <ubanus@users.sf.net>'
__version__ = '0.1'

from elinks.mapping import MAPPING
from codecs import register_error as _register_error

def handler(exception):
	'''The elinks-like encoding error handler.'''
	if isinstance(exception, (UnicodeEncodeError, UnicodeTranslateError)):
		return ''.join(MAPPING.get(ch, u'*') for ch in exception.object[exception.start:exception.end]), exception.end
	else:
		raise TypeError("Don't know how to handle %s in error callback" % exception.__class__.__name__)

_register_error('elinks', handler)

# vim:ts=4 sw=4

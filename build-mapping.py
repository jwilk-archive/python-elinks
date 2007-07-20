from sys import stderr
from urllib2 import urlopen
from warnings import warn
import re

_re = re.compile(
	r'''
	^	U[+] (?P<code> [0-9a-f]{4} ) : (?P<replace> .* ) $ |
	^	(?P<hexreplace> 0x[0-9a-f]{2} )
		(?P<codes> 
			(?:
				(?: \s+ U[+] (?: [0-9a-f]{4} ) ) |
				(?: \s+ U[+] (?: [0-9a-f]{4} ) - U[+] (?: [0-9a-f]{4} ) )
			)+
		) (?: \s*[#].* )? $ |
	^	(?P<idem> 0x20-0x7e \s+ idem ) $ |
	^	(?P<fwdt> 0x21-0x7e \s+ U[+]ff01-U[+]ff5e ) $
	''',
	re.VERBOSE | re.IGNORECASE)

_re_codes = re.compile(
	r'''
		U[+] ( [0-9a-f]{4} ) - U[+] ( [0-9a-f]{4} ) |
		U[+] ( [0-9a-f]{4} )
	''',
	re.VERBOSE | re.IGNORECASE)

_re_ignore = re.compile('^(?: [#] | D1 | Mus-ascii | $)', re.VERBOSE)

_re_oct_escape = re.compile(r'\\([0-7]{3})')

mapping = {}

def update(code, replace):
	try:
		mapping[unichr(code)] = unicode(replace)
	except Exception:
		print >>stderr, hex(code), repr(replace)

for line in urlopen('http://repo.or.cz/w/elinks.git?a=blob_plain;f=Unicode/7bitrepl.lnx;hb=elinks-0.12'):
	line = line.strip()
	if not line:
		continue
	if _re_ignore.match(line):
		continue
	m = _re.match(line)
	if not m:
		print >>stderr, 'Bogus line: ' + line
	else:
		code = hexreplace = codes = idem = fwdt = None
		locals().update(m.groupdict())
		if code:
			code = int(code, 16)
			replace = _re_oct_escape.sub(lambda m: chr(int(m.group(1), 8)), replace)
			update(code, replace)
		elif hexreplace:
			replace = chr(int(hexreplace, 16))
			codes = _re_codes.findall(codes)
			if not codes:
				raise Exception('Internal error')
			for code in codes:
				if code[2]:
					code = int(code[2], 16)
					update(code, replace)
				else:
					for code in xrange(int(code[0], 16), int(code[1], 16) + 1):
						update(code, replace)
		elif idem:
			for code in xrange(0x20, 0x7f):
				update(code, chr(code))
		elif fwdt:
			for code in xrange(0xff01, 0xff5f):
				update(code, chr(code - 0xff00 + 0x20))
		else:
			raise Exception('Internal error')

print 'MAPPING = ', mapping

# vim:ts=4 sw=4 noet

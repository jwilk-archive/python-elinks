# encoding=UTF-8

# Copyright © 2007, 2010 Jakub Wilk <jwilk@jwilk.net>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from sys import stderr
from urllib2 import urlopen
from warnings import warn
from pprint import pprint
import re

class InternalError(Exception):
    def __init__(self):
        Exception.__init__(self, 'Internal error')

_re = re.compile(
    r'''
    ^   U[+] (?P<code> [0-9a-f]{4} ) : (?P<replace> .* ) $ |
    ^   (?P<hexreplace> 0x[0-9a-f]{2} )
        (?P<codes>
            (?:
                (?: \s+ U[+] (?: [0-9a-f]{4} ) ) |
                (?: \s+ U[+] (?: [0-9a-f]{4} ) - U[+] (?: [0-9a-f]{4} ) )
            )+
        ) (?: \s*[#].* )? $ |
    ^   (?P<idem> 0x20-0x7e \s+ idem ) $ |
    ^   (?P<fwdt> 0x21-0x7e \s+ U[+]ff01-U[+]ff5e ) $
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
    mapping[unichr(code)] = unicode(replace)

print '''# encoding=UTF-8

# This file was automatically generated from the Unicode/7bitrepl.lnx file of
# ELinks 0.12 distribution. ELinks is free free software; you can redistribute
# it and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; version 2 dated June, 1991.
'''
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
                raise InternalError()
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
            raise InternalError()

print 'MAPPING = \\'
pprint(mapping, width=1)

# vim:ts=4 sw=4 et

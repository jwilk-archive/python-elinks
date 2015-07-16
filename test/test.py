#!/usr/bin/python
# encoding=UTF-8

# Copyright © 2007-2015 Jakub Wilk <jwilk@jwilk.net>
#
# This package is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.

import elinks

try:
    unicode
except NameError:
    # Python 3.X
    def u(s):
        return s
    def b(s):
        return s.encode('UTF-8')
else:
    # Python 2.X
    def u(s):
        return s.decode('UTF-8')
    def b(s):
        return s

def test_elinks():
    s = u('Różowy słoń nie zechce usiąść na tępych gwoździach…')
    t = b('Rozowy sl/on nie zechce usiasc na tepych gwozdziach...')
    encoded_s = s.encode('ASCII', 'elinks')
    assert encoded_s == t, '{s!r} != {t!r}'.format(s=encoded_s, t=t)

if __name__ == '__main__':
    test_elinks()

# vim:ts=4 sts=4 sw=4 et

#!/usr/bin/python
# encoding=UTF-8

import elinks

def test_elinks():
    s = u'Różowy słoń nie zechce usiąść na tępych gwoździach…'
    t = 'Rozowy sl/on nie zechce usiasc na tepych gwozdziach...'
    assert s.encode('ASCII', 'elinks') == t

# vim:ts=4 sw=4 noet

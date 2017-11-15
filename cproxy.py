# -*- coding: utf-8 -*-
from db import *
from testproxy import getproxy, testall


def insertdb():
    proxys = getproxy()
    sqls = formatSQL(proxys, 'ADD')
    act(sqls)


def updatedb():
    proxys = select(100)
    _proxys = [[proxy[0], proxy[1]] for proxy in proxys]
    print '_proxys', _proxys
    new_proxys = testall(_proxys)
    print 'new_proxys', new_proxys
    _new_proxys = [[new_proxy[0], new_proxy[1]] for new_proxy in new_proxys]
    print '_new_proxys', _new_proxys
    del_proxys = [x for x in _proxys if x not in _new_proxys]
    print "del_proxys", del_proxys
    sqls_del = formatSQL(del_proxys, 'DEL')
    sqls_mod = formatSQL(new_proxys, 'MOD')
    act(sqls_del)
    act(sqls_mod)

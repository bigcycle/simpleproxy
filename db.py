import sqlite3
import time


proxydb = 'proxys.db'
proxylog = 'message.log'


def logger(*args):
    message = ''
    for arg in args:
        message += arg
    with open(proxylog, 'a') as f:
        f.write(getCurrentTime() + message + '\n')


def getCurrentTime():
    return time.strftime('[%Y-%m-%d %H:%M:%S]:',
                         time.localtime(time.time()))


def formatSQL(proxies, action):
    sqls = []
    if proxies is None:
        print 'No proxy found.'
        return sqls
    if action == 'ADD':
        for proxy in proxies:
            sql = "INSERT OR IGNORE INTO PROXY (IP,PORT,FP,DELAY) VALUES ('%s', '%s', '%s', %f)" % (
                proxy[0], proxy[1], proxy[0] + ':' + proxy[1], proxy[2])
            sqls.append(sql)
    elif action == 'DEL':
        for proxy in proxies:
            sql = "DELETE FROM PROXY WHERE IP='%s' AND PORT='%s'" % (
                proxy[0], proxy[1])
            sqls.append(sql)
    elif action == 'MOD':
        for proxy in proxies:
            sql = "UPDATE PROXY SET DELAY=%f WHERE IP='%s' AND PORT='%s'" % (
                proxy[2], proxy[0], proxy[1])
            sqls.append(sql)
    else:
        exit(1)
    return sqls


def act(sqls):
    conn = sqlite3.connect(proxydb)
    logger("Opened database successfully")
    result = ''
    for sql in sqls:
        try:
            cursor = conn.execute(sql)
            print 'execute:', sql
            result = cursor.fetchall()
            print 'result:', result
        except Exception, e:
            logger("SQL ERROR:", sql)
            logger(str(e))
            conn.rollback()
    conn.commit()
    logger("SQL Operations Succeed!")
    conn.close()
    return result


def select(num, fast=False):
    if fast is True:
        sql = ["SELECT * FROM PROXY ORDER BY DELAY LIMIT %s" % str(num)]
    else:
        sql = ["SELECT * FROM PROXY LIMIT %s" % str(num)]
    result = act(sql)
    return [[x[1], x[2], x[4]] for x in result]


def query():
    sql = ["SELECT COUNT(*) FROM PROXY"]
    print act(sql)[0][0]

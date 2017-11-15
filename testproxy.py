import commands
# from ip181 import ip181
from ip66 import ip66
# from cproxy.kuaidaili import kuaidaili
from xici import xici
from f31 import f31
import threading

vproxy = []
testaddr = 'http://www.baidu.com'


class MyThread(threading.Thread):

    def __init__(self, target, arg):
        super(MyThread, self).__init__()
        self.target = target
        self.arg = arg

    def run(self):
        self.target(self.arg)


def testproxy(proxy):
    global vproxy
    cmd = 'curl --connect-timeout 3 -m 3 -x %s:%s %s' % (proxy[0], proxy[1], testaddr)
    code, result = commands.getstatusoutput(cmd)
    print code, cmd
    if code == 0:
        cmd2 = 'curl -o /dev/null -x %s:%s -s -w %%{time_total} %s' % (proxy[0], proxy[1], testaddr)
        result = commands.getoutput(cmd2)
        print result
        _proxy = list(proxy)
        _proxy.append(float(result))
        vproxy.append(_proxy)


def testall(proxys):
    # global vproxy
    # vproxy = []
    num = len(proxys)
    threads = []
    if num > 0:
        for i in xrange(0, num):
            my_thread = MyThread(testproxy, proxys[i])
            threads.append(my_thread)
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
    return vproxy


def getproxy():
    try:
        proxys = xici()
        proxys += ip66()
        proxys += f31()
    except Exception as e:
        print e
    return testall(proxys)


# if __name__ == '__main__':
    # proxys3 = xici()
    # testall(proxys3)
    # print "xici:", len(vproxy)
    # proxys2 = ip66()
    # testall(proxys2)
    # print "ip66:", len(vproxy)
    # proxys1 = ip181()
    # testall(proxys1)
    # print "ip181:", len(vproxy)
    # proxys4 = f31()
    # testall(proxys4)
    # print "f31:", len(vproxy)

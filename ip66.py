import requests
import re
import urllib


def ip66(getnum='30', isp='0', anonymoustype='3', start='', ports='', export='', ipaddress='', area='1', proxytype='2', api='66ip'):
    API = "http://www.66ip.cn/nmtq.php?%s"
    paras = {
        "proxytype": proxytype,
        "area": area,
        "anonymoustype": anonymoustype,
        "isp": isp,
        "start": start,
        "getnum": getnum,
        "api": api,
        "export": export,
        "ipaddress": ipaddress,
        "ports": ports
    }
    para = urllib.urlencode(paras)
    url = API % para
    page = requests.get(url).text
    pattern = re.compile('</script>(.*?)</div>', re.S)
    result = re.search(pattern, page).group(1).split('<br />')
    list = [x.strip().split(':') for x in result[:-1]]
    return list


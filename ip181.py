# -*- coding=UTF-8 -*-
import requests
import re


def ip181():
    vpxy = []
    url = 'http://www.ip181.com/'
    page = requests.get(url)
    page.encoding = 'gbk'
    pattern = re.compile(
        '<tr.*?>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?</tr>',
        re.S)
    proxys = re.findall(pattern, page.text)
    for proxy in proxys[1:]:
        if proxy[2] == u'高匿':
            vpxy.append([proxy(0), proxy(1)])
    return vpxy

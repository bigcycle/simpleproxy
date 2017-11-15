import requests
import re


def f31():
    url = 'http://31f.cn/anonymous-proxy/'
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    headers = {'User-Agent': user_agent}
    page = requests.get(url, headers=headers)
    pattern = re.compile('<tr>\s<td.*?<td>(.*?)</td>\s<td>(.*?)</td>\s<'
                         'td.*?<td.*?<td.*?<td.*?<td.*?/tr>',
                         re.S)
    proxys = re.findall(pattern, page.text)
    return proxys

import requests
import re


def kuaidaili():
    urls = ['http://www.kuaidaili.com/free/inha',
            'http://www.kuaidaili.com/free/intr']
    proxys = []
    for url in urls:
        page = requests.get(url)
        pattern = re.compile(
            '<tr>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?</tr>',
            re.S)
        proxys += re.findall(pattern, page.text)
    return proxys


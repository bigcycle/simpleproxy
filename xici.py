import requests
import re


def xici():
    url = 'http://www.xicidaili.com/nn/'
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    headers = {'User-Agent': user_agent}
    page = requests.get(url, headers=headers)
    pattern = re.compile('<tr class=.*?>.*?<td class="country">.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?</tr>', re.S)
    proxys = re.findall(pattern, page.text)
    return proxys

# print xici()

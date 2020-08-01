from lxml.html import fromstring
from random import randint
import requests
import re

def get_list():
    html = requests.get('https://free-proxy-list.net/')
    parser = fromstring(html.text)
    proxylist = []
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = i.xpath('.//td[1]/text()')[0] + ':' + i.xpath('.//td[2]/text()')[0]
            proxylist.append(proxy)
    return proxylist

def get_proxy():
    proxylist = get_list()
    url = 'https://httpbin.org/ip'
    working_proxy = False

    while working_proxy == False:
        index = randint(0, len(proxylist) - 1)
        proxy = proxylist[index]
        try:
            response = requests.get(url,proxies={"http": proxy, "https": proxy})
            working_proxy = True
        except:
            proxylist.pop(index)

    return proxy

print(get_proxy())

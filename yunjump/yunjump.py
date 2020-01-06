#coding:utf-8
import requests

import urllib3
urllib3.disable_warnings()
import re
from urllib.parse import urljoin

def stringToHex(string):
    length = len(string)
    hex_string = str()
    for i in range(length):
        hex_string += hex(ord(string[i]))[2:]
        print (hex_string)
    return hex_string

def get_cookie(url):
    hex_string = stringToHex(url)
    cookie = {"srcurl": hex_string, "path": "/"}
    return cookie
def get_datas():
    url = "http://www.hbyinfa.gov.cn/cishan/"
    s = requests.Session()
    r = s.get(url)
    print(r.text)
    url_2 = re.compile("self\.location\s*=\s*\"(.*?)\"").findall(r.text)[0]
    screen_date = "1920,1080"
    url_2 = url_2 + stringToHex(screen_date)
    url_2 = urljoin(url, url_2)
    print (url_2)
    cookie = get_cookie(url)
    print (cookie)
    s.cookies.update(cookie)
    r2 = s.get(url_2)
    print (r2.text)
    url3 = re.compile("self\.location\s*=\s*\"(.*?)\"").findall(r2.text)[0]
    r3 = s.get(url3)
    r3.encoding = "gbk"
    print (r3.text)
get_datas()

import requests
import re
import execjs
import urllib3
urllib3.disable_warnings()
url = 'https://blog.csdn.net/qq_32786139/article/details/103666149'
headers = dict()
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' \
                        ' Chrome/73.0.3683.75 Safari/537.36'
session = requests.session()
response = session.get(url, headers=headers, verify=False)
html_js = response.content.decode()
arg1 = re.search(r'var arg1=\'(.*)\';', html_js).group(1)
with open('sojson_CSDN.js', 'r') as f:
    SDK = f.read()
ctx = execjs.compile(SDK)
acw_sc__v2 = ctx.call('SDK',  arg1)
print(acw_sc__v2)
cookies = {'acw_sc__v2': acw_sc__v2}
response = session.get(url, headers=headers, verify=False, cookies=cookies)
html = response.content.decode()
print(html)
print(acw_sc__v2)
print(acw_sc__v2)
print(acw_sc__v2)
print(acw_sc__v2)


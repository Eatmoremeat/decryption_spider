#coding:utf-8
import requests
import re
import execjs


url = "http://hetda.hefei.gov.cn/"
headers = {
    # 'Cookie': "__jsluid=4f7efbfcbce6a01529ec0003981bb482; UM_distinctid=16972763956ccc-0e4c874106f6f7-36677905-13c680-16972763957a24; __jsluid_h=02dec99ec66ebb0d072094fbcc2096cd; SECTOKEN=6959647022540130109; gsxtBrowseHistory1=%0FS%04%06%1D%04%1D%10SNS%24%26%3B%22%3D%3A71%3A%3B01%3A%219%40%40DDDD5DGEALASXS%11%1A%00%1A%15%19%11SNS%E5%8C%BA%E4%B9%8E%E6%8B%B4%E6%9D%9B%E6%9D%BD%E9%98%A4%E5%84%98%E5%8E%8CSXS%11%1A%00%00%0D%04%11SNEEAFXS%02%1D%07%1D%00%00%1D%19%11SNEABFLMDFADFD%40%09; __jsl_clearance=1564905820.383|0|vzFdCeOoS3weRmIVyf2jGNOjMjI%3D; CNZZDATA1261033118=1413769021-1552399297-http%253A%252F%252Fwww.gsxt.gov.cn%252F%7C1564904187; JSESSIONID=5EE8F665B29D6AE241EC5E8677876E0D-n2:1; tlb_cookie=S172.16.12.131",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
    }
session = requests.session()
response = session.get(url, headers=headers)
# print(response.text)

# 生成cookie中的字段
res = re.findall('<script>(.*?)</script', response.text)[0]

js = res.replace('eval', 'var aaa=')
chaojijs = execjs.compile(js)
js2 = chaojijs.eval("aaa")
# print (js2)

js3 = re.search("document.(cookie.*?)\+\';Expires", js2).group(1)
other_param = 'window={};' + js3
ctx1 = execjs.compile(other_param)
jsl_params = ctx1.eval('cookie')
# print (jsl_params)
#
# print response.cookies
cookies = jsl_params.split('=')
session.cookies.set(cookies[0], cookies[1])
session.get(url, headers=headers)
# print(session.cookies)
cookies = requests.utils.dict_from_cookiejar(session.cookies)
res = session.get(url, headers=headers,cookies=cookies)
if res.status_code == 200:
    res.encoding = res.apparent_encoding
    print(res.text)

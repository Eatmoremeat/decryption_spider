#coding:utf-8
from lxml import etree
import requests
import execjs
url = 'http://www.pbc.gov.cn/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/73.0.3683.75 Safari/537.36',
}
session = requests.session()

# -------- 构造可执行js 并把需求结果生成全局变量 ----------
js_href = session.get(url).text
js_href = etree.HTML(js_href).xpath('//script/text()')[0]
js_href = '''
const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
window = dom.window;
document = window.document;
XMLHttpRequest = window.XMLHttpRequest;
''' + js_href
js_href = js_href.replace('window[_0x56ae(\'0x3c\',\')9A&\')]=', 'a = ').replace('atob(', 'window.atob(')
# -------------------- js构造结束 ----------------------

com = execjs.compile(js_href)
print (com)
res = com.eval('a')
print(res,)
session_url = 'http://www.pbc.gov.cn/' + res
response = session.get(session_url)
response.encoding = 'utf-8'
print(response.text)

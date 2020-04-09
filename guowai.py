import requests
import re
from lxml import etree
import json
import execjs
headers = {

# "cookie": "sucuri_cloudproxy_uuid_328333d9a=1f979e12ce3c72341f556894cb157ae0;",

# "referer": "https://www.fraserinstitute.org/",

"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
}
s=requests.session()
response = s.get(
    'https://www.fraserinstitute.org/',headers=headers)
response.encoding = 'utf-8'
print(response.text)
js_1=re.search('''script>(.*?)</script''',response.text).group(1).replace('e(r);','')
jscontext = execjs.compile(js_1)
r= jscontext.eval('r')
js_2=r.replace('document.','').replace('location.reload();','')
jscontext_2=execjs.compile(js_2)
cookie=jscontext_2.eval('cookie').split("path=")[0]
print(cookie)
headers2={


 "cookie": cookie,

# "referer": "https://www.fraserinstitute.org/",

"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
}

response2=requests.get('https://www.fraserinstitute.org/',headers=headers2)
print(response2.text)

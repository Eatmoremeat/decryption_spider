import requests
import re
s=requests.Session()
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'

}
res=s.get('http://www.qjbxw.com/forum-137-1.html',headers=headers)
print(res.text)
one_cookie=re.search('''document.cookie\s*=\s*'(.*?)path''',res.text).group(1)
headers["Cookie"]=one_cookie
res2=s.get('http://www.qjbxw.com/forum-137-1.html',headers=headers)
print(res2.text)

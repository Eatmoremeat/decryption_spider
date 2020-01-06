import requests
import urllib3
urllib3.disable_warnings()
import time
#
# url = 'https://www.hengyirong.com/about/a_news/'
import hashlib


def get_header(url, data):
    headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/73.0.3683.75 Safari/537.36',
        'Host': 'www.hengyirong.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3',
    }
    times = str(int(time.time()))
    list_1 = [
        url,
        "1.0.0",
        "pc",
        "DHz@uEun&k^LtqbhYqUN5wetfaO8p2",
        times,
        "",
        "pc",
        "1.2.0",
        data,
    ]
    res_2 = '|'.join(list_1)
    print(res_2)
    m = hashlib.md5()
    m.update(res_2.encode(encoding='UTF-8'))
    x_sign = m.hexdigest()
    headers['x-appid'] = 'pc'
    headers['x-client-info'] = 'pc'
    headers['x-t'] = times
    headers['x-ver'] = '1.1'
    headers['x-client-version'] = '1.2.0'
    headers['x-v'] = '1.0.0'
    headers['x-access-token'] = ''
    headers['x-sign'] = x_sign
    headers['Referer'] = 'https://www.hengyirong.com/about/a_news/'
    headers['Content-Type'] = 'application/json;charset=UTF-8'
    return headers


# url = 'https://www.hengyirong.com/api/v1/content/catalog-list'
session = requests.session()
# data = '{"id":9}'
# headers = get_header("/v1/content/catalog-list", data)


# response = session.post(url, data=data, headers=headers, verify=False)


url_2 = 'https://www.hengyirong.com/api/v1/content/catalog-detail'
data = '{"catalog_id":"24","page":1}'
headers = get_header("/v1/content/catalog-detail", data)
response_2 = session.post(url_2, data=data, headers=headers, verify=False)
print (response_2.text)


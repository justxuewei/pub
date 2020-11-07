import requests
import os
from urllib import parse

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6",
    "cache-control": "no-cache",
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.111 Mobile Safari/537.36 "
}

s = requests.Session()
s.headers = headers

username = os.environ["BUPT_LOGIN_USER"]
password = os.environ["BUPT_LOGIN_PASS"]

form_data = {
    "user": username,
    "pass": password
}
data = parse.urlencode(form_data)

login_response = s.post("http://10.3.8.211/login", data=data)
if login_response.status_code == 200:
    print("Login OK.")
else:
    print("Login is failed.")

import requests
from urllib import parse
import sys

# python script for network authentication login at BUPT
# usage: python3 bupt_login.py -u <USERNAME> -p <PASSWORD>
if __name__ == "__main__":
    argv = sys.argv

    usage_prompt = "Usage: python3 bupt_login.py -u <USERNAME> -p <PASSWORD>"
    if len(argv) != 4 and "-u" not in argv and "-p" not in argv:
        print(usage_prompt)
        exit(1)
    username = None
    password = None
    for i in range(len(argv)):
        if argv[i] == "-u" and i + 1 < len(argv):
            username = argv[i+1]
        elif argv[i] == "-p" and i + 1 < len(argv):
            password = argv[i+1]
    if username is None or password is None:
        print(usage_prompt)
        exit(1)

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

    form_data = {
        "user": username,
        "pass": password
    }
    data = parse.urlencode(form_data)

    login_response = s.post("http://10.3.8.211/login", data=data)
    if login_response.status_code == 200:
        print("Login OK.")
        exit(0)
    else:
        print("Login is failed.")
        exit(1)

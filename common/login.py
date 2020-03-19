import requests
from model import fixconfig, read_yaml


def logging(_url, _username, _pwd):
    data = {
        'account': _username,
        'password': _pwd
        }
    r = requests.post(url=_url, data=data)
    result = r.json()

    return result


if __name__ == "__main__":
    l1 = read_yaml()[0]['baseurl']
    l2 = read_yaml()[1]['url']
    url = l1+l2
    username = read_yaml()[1]['account']
    pwd = read_yaml()[1]['password']
    result = logging(url, username, pwd)
    token = result['data']['token']

    fixconfig("token",token)  # 修改token的值为本次登录的token

    print(result)
import requests


def importdata(_url, token, a, b):    # 导入客户数据
    data = {
        'customer_name': a,
        'source': 1,
        'website': b
    }
    header = {'Authorization': token}
    r = requests.post(url=_url, headers=header, data=data)
    result = r.json()
    return result


def importContactData(_url, token, a, b, c):    # 导入联系人数据
    data = {
        'customer_id': a,
        'first_name': b,
        'mobile': c,
        'source': 1
    }
    header = {'Authorization': token}
    r = requests.post(url=_url, headers=header, data=data)
    result = r.json()
    return result

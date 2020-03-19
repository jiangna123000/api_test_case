import requests
from model import read_yaml, readconfig


def set_show_fields(url, header):
    a = read_yaml()[7]['fields']
    # print(a)
    # da = json.dumps(a)  # 把yaml里的数据转换成json格式
    data = {
        'type': 3,
         'fields': a,
        'source': "1",
        'version_code': "7"
        }
    r = requests.post(url=url, headers=header, data=data, stream=True)
    result = r.json()
    return result


def get_show_fields(url, header):
    data = {
        'type': 2,
        'version_code': "7",
        'source': "1"
    }
    r = requests.post(url=url, headers=header, data=data, stream=True)
    result = r.json()
    return result




if __name__ == '__main__':
    token = readconfig('token')
    print(set_show_fields('https://www.scrm365.cn/api/scrm/setShowFields', header={'Authorization': token}))



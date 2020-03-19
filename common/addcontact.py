import requests, time, json
from model import readconfig, read_yaml


def add_contact(url, _token):

    a = read_yaml()[6]['data']
    da = json.dumps(a)    # 把yaml里的数据转换成json格式
    data = {
       'form_json_data': da,
        'from_email': '0',
        'source': '1',
    }
    header = {'Authorization': _token}
    r = requests.post(url=url, headers=header, data=data, stream=True)
    result = r.json()
    return result


if __name__ == '__main__':
    i = '%s' % time.strftime('%j'+'%S', time.localtime(time.time()))  # 一年中的第几天+秒数
    print(i)
    token = readconfig('token')
    c = add_contact(url='https://www.scrm365.cn/api/scrm/contactAdd', _token=token)
    print(c)
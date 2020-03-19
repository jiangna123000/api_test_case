import requests, os, time
from model import readconfig, read_yaml


def importAnalysis(_url, _token, n):   # 导入解析文件
    data = {
        '_gouuse_token': _token,
        'type': n   # 1-联系人，0-客户
        }
    # 获取当前脚本所在文件夹路径
    curpath = os.path.abspath(os.path.dirname(os.getcwd()))
    file_home = curpath+r"\SCRM_API_TEST\file\contact.xlsx"   # run 跑的时候用
    # file_home = curpath + r"\file\contact.xlsx"  # run 跑的时候加上\SCRM_API_TEST   headers=header
    with open(file_home, 'rb') as f:
        files = {'file': ('contact.xlsx', f, 'application/octet-stream')}
        r = requests.post(url=_url, data=data, files=files)
        result = r.json()

    return result


if __name__ == '__main__':
    l1 = read_yaml()[0]['baseurl']
    l2 = read_yaml()[3]['url']
    url = l1+l2
    token = readconfig('token')
    r = importAnalysis(_url=url, _token=token, n=1)
    print(r)
    # curpath = os.path.abspath(os.path.dirname(os.getcwd()))
    # file_home = curpath+r"\model\contact.xlsx"
    # print(file_home)
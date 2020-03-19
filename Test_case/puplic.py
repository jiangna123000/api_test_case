from model import SetUpTearDown, read_yaml, readconfig, Log, fixconfig
from common import contact_required


def test_contact():
    """测试联系人列表，接口地址:/api/scrm/contacts"""
    l2 = read_yaml()[2]['url']
    l1 = read_yaml()[0]['baseurl']
    url = l1 + l2
    token = readconfig('token')
    result = contact_required(_url=url, _token=token)
    return result







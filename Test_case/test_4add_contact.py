from model import SetUpTearDown, read_yaml, readconfig
from common import add_contact
import unittest,time


# @unittest.skip("暂时跳过")
class TestAddCantact(SetUpTearDown):

    def test_addcontact(self):
        """添加联系人所有字段值，接口地址:/api/scrm/contactAdd"""
        l2 = read_yaml()[6]['url']
        token = readconfig('token')
        url = self.l + l2
        result = add_contact(url=url, _token=token)
        if result['code'] != 0:
            if result['msg'] in "手机号/邮箱/座机至少填一项":
                 i = str('%s' % time.strftime('%j' + '%S', time.localtime(time.time())))  # 一年中的第几天+秒数
                 read_yaml()[6]['data']['email'] = ""+i+'@qq.com'""
                 return self.test_addcontact
        else:
            return result







from common import set_show_fields,get_show_fields
from model import read_yaml, SetUpTearDown, fixconfig, readconfig
import random


class TestSetShowFields(SetUpTearDown):
    def test_set_showfields(self):
        """修改联系人自定义列表头，接口地址:/api/scrm/setShowFields"""
        url = self.l+read_yaml()[7]['url1']
        token = readconfig('token')
        result = set_show_fields(url=url, header={'Authorization': token})
        print(result)
        return result

    def test_get_showfields(self):
        """获取联系人自定义列表头，接口地址:/api/scrm/getShowFields"""
        url = self.l + read_yaml()[7]['url2']
        result = get_show_fields(url=url, header=self.header)
        a = result['data']
        print(a)
        return result

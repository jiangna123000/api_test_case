from model import SetUpTearDown, read_yaml, readconfig, Log, fixconfig
from common import contact_required, contact_other, contact_sort, contact_search, customer_required
import unittest

#@unittest.skip
class TestContactList(SetUpTearDown):
    def test_contact(self):
        """测试联系人列表，接口地址:/api/scrm/contacts"""
        l2 = read_yaml()[2]['url']
        url = self.l + l2
        token = readconfig('token')
        result = contact_required(_url=url, _token=token)
        self.assertEqual(result['code'], 0)
        # 打印日志到logs
        log = Log()
        log.debug('联系人列表返回信息：%s' % result)
        fixconfig(key='contact_total', value=str(result['page_info']['total']))
        return result

# @unittest.skip
    def test_contact_other(self):
        """联系人列表非必填项，接口地址:/api/scrm/contacts"""
        for i in self.contactlist:
            l2 = read_yaml()[2]['url']
            url = self.l + l2
            token = readconfig('token')
            list = self.test_contact()
            if i == "system_grade_level":  # 筛选系统评级为1时
                print('筛选系统评级为1时')
                result, t = contact_other(_url=url, _token=token, key=i, value=1, listresult=list)
                self.assertEqual(result['code'], 0)
                self.assertEqual(result['page_info']['total'], t)
            if i == "tag_ids":  # 筛选标签为“中国通”
                print('筛选标签为“中国通”')
                result, t = contact_other(_url=url, _token=token, key=i, value=2737, listresult=list)
                self.assertEqual(result['code'], 0)
                self.assertEqual(result['page_info']['total'], t)
            if i == "state_id":  # 国家为“中国”
                print('筛选国家为“中国”')
                result, t = contact_other(_url=url, _token=token, key=i, value=43, listresult=list)
                self.assertEqual(result['code'], 0)
                self.assertEqual(result['page_info']['total'], t)
            if i == "is_worktime":  # 是工作时间
                print('筛选是工作时间')
                result = contact_sort(_url=url, _token=token, key=i, value=1)
                self.assertEqual(result['code'], 0)
            if i == "saleman":  # 跟进人是我自己
                print('筛选跟进人是我自己')
                result, t = contact_other(_url=url, _token=token, key=i, value=100058471, listresult=list)
                self.assertEqual(result['code'], 0)
                self.assertEqual(result['page_info']['total'], t)
            if i == "keywords":  # 关键词查询按照所属客户查
                print('关键词查询按照所属客户查')
                result, t = contact_search(_url=url, _token=token, key=i, value='阿富汗111', listresult=list,
                                           cod='customer_name', price='阿富汗111')
                self.assertEqual(result['code'], 0)
                self.assertEqual(result['page_info']['total'], t)
            if i == "sort_system_grade_level":  # 按系统评级排序。 desc降序，asc升序
                print('按系统评级排序')
                result = contact_sort(_url=url, _token=token, key=i, value='asc')
                self.assertEqual(result['code'], 0)
            if i == "sort_recent_action_time":  # 按最近动态时间排序 desc降序，asc升序
                print('按最近动态时间排序')
                result = contact_sort(_url=url, _token=token,  key=i, value='desc')
                self.assertEqual(result['code'], 0)
            if i == "sort_recent_contact_time":  # 按最近联系时间排序 desc降序，asc升序
                print('按最近联系时间排序')
                result = contact_sort(_url=url, _token=token, key=i, value='desc')
                self.assertEqual(result['code'], 0)
            if i == "life_cycle":  # 生命周期 1 新建客户
                print('按生命周期')
                result, t = contact_other(_url=url, _token=token, key=i, value=1, listresult=list)
                self.assertEqual(result['code'], 0)
                self.assertEqual(result['page_info']['total'], t)
            if i == "first_letter":  # 按最近联系时间排序 desc降序，asc升序
                print('按最近联系时间排序')
                result = contact_sort(_url=url, _token=token,  key=i, value='desc')
                self.assertEqual(result['code'], 0)
            if i == "group_id":  # 跟进人分组主要联系人的
                print('跟进人分组主要联系人的')
                result, t = contact_other(_url=url, _token=token, key=i, value=4716, listresult=list)
                self.assertEqual(result['code'], 0)
                self.assertEqual(result['page_info']['total'], t)
            if i == "search_source":  # 跟来源展会筛选
                print('跟来源展会筛选')
                result, t = contact_search(_url=url, _token=token, key=i, value=2249, listresult=list,
                                           cod='source', price=2249)
                self.assertEqual(result['code'], 0)
                self.assertEqual(result['page_info']['total'], t)

    def test_custmoser(self):   # 获取客户列表
        """获取客户列表，接口地址:/api/scrm/contacts"""
        l2 = read_yaml()[5]['url']
        url = self.l + l2
        token = readconfig('token')
        result = customer_required(_url=url, _token=token)
        self.assertEqual(result['code'], '0')
        # 打印日志到logs
        log = Log()
        log.debug('客户列表返回信息：%s' % result)
        fixconfig(key='customer_total', value=str(result['data']['page_info']['total']))
        return result
























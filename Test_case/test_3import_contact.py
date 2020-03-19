from model import readconfig, read_yaml, SetUpTearDown, change_excel
from common import importAnalysis, importdata, importContactData, customer_required, contact_required
import time, unittest
from BeautifulReport import BeautifulReport


# @unittest.skip
class TestImportContact(SetUpTearDown):
    customer, website, cname, mobile = change_excel()
    l1 = read_yaml()[0]['baseurl']
    token = readconfig('token')

    @unittest.skip("暂时跳过")  # 不执行该用例
    def test_importAnalysis(self):  # 解析联系人、客户excel表
        """解析联系人、客户excel表，接口地址:/api/scrm/importAnalysis"""
        l2 = read_yaml()[3]['url']
        url = self.l1 + l2

        t = time.time()
        if t % 2 == 0:
            result = importAnalysis(_url=url, _token=self.token, n=0)   # 客户列表导入添加联系人 n=1和客户 n=0文件
        else:
            result = importAnalysis(_url=url, _token=self.token, n=1)  # 联系人列表导入添加联系人 n=1 和客户 n=0文件
        self.assertEqual(result['code'], 0)

    def test_import_data(self):   # 导入客户数据
        """导入客户数据，接口地址:/api/scrm/importData"""
        l2 = read_yaml()[4]['url1']
        url = self.l1 + l2
        result = importdata(_url=url, token=self.token, a=self.customer, b=self.website)
        if result['code'] == 0:
            # 断言列表中total多了一个新加的客户
            a = int(readconfig(key='customer_total'))+1
            url2 = read_yaml()[2]['url']
            url3 = self.l + url2
            r = customer_required(_url=url3, _token=self.token)['page_info']['total']
            self.assertEqual(a, r)
        else:
            print(result['msg'])

    def test_importContactData(self):   # 导入联系人数据
        """导入联系人数据，接口地址:/api/scrm/importContactData"""
        l2 = read_yaml()[4]['url2']
        url = self.l1 + l2
        result = importContactData(_url=url, token=self.token, a=self.customer, b=self.cname, c=self.mobile)
        if result['code'] == 0:
            self.assertEqual(result['code'], 0)
            # 断言列表中total多了一个新加的联系人
            b = int(readconfig(key='contact_total'))+1
            url2 = read_yaml()[2]['url']
            url3 = self.l + url2
            r = contact_required(_url=url3, _token=self.token)['page_info']['total']
            self.assertEqual(b, r)
        else:
            print(result['msg'])








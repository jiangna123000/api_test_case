from model import SetUpTearDown, read_yaml
from common import contactmerge, contact_search
from Test_case.puplic import test_contact


class TestcontactMerge(SetUpTearDown):
    def test_contactMerge(self):
        """合并联系，接口地址:/api/scrm/contactMerge"""
        list = test_contact()
        merge_contacts_id = list['data'][0]['contacts_id']
        contacts_id = list['data'][1]['contacts_id']
        url = self.l+read_yaml()[8]['url']
        result = contactmerge(url=url, a=contacts_id, b=merge_contacts_id, header=self.header)
        self.assertEqual(0, result['code'])














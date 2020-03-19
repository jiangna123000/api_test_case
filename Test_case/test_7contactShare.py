from model import SetUpTearDown,read_yaml,readconfig
from common import get_shares_contacts, contactShare
from Test_case.puplic import test_contact


class TestContactShare(SetUpTearDown):
    contacts_id = test_contact()['data'][0]['contacts_id']

    def test_getcontactshare(self):
        """共享联系，接口地址:/api/scrm/getSharesContacts"""
        url = self.l+read_yaml()[9]['url1']
        result = get_shares_contacts(url=url, contacts_id=self.contacts_id, header=self.header)
        self.assertEqual(0, result['code'])

    def test_contactshare(self):
        """共享联系，接口地址:/api/scrm/contactShare"""
        url = self.l+read_yaml()[9]['url2']
        member_id = readconfig('member_id')
        result = contactShare(url=url, contacts_id=self.contacts_id, header=self.header, member_id=member_id)
        self.assertEqual(0, result['code'])

import unittest
from model import read_yaml
from model.config import readconfig



class SetUpTearDown(unittest.TestCase):

    def setUp(self):
        self.l = read_yaml()[0]['baseurl']
        self.contactlist = read_yaml()[2]['contact_list']
        print("开始执行！")
        self._token = readconfig('token')
        self.header = {'Authorization': self._token}

    def tearDown(self):
        print("执行结束！")


if __name__ =="__main__":
    a =SetUpTearDown(unittest.TestCase).l
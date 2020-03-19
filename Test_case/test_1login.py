from model import SetUpTearDown, fixconfig, Log, read_yaml, coloring
from common import logging


class TestLogin(SetUpTearDown):
    def test_normal_login(self):
        """测试正常登陆，接口地址：/api/auth_center/v3/login"""
        l1 = self.l
        l2 = read_yaml()[1]['url']
        url = l1 + l2   # 拼接url
        username = read_yaml()[1]['account']
        pwd = read_yaml()[1]['password']
        result = logging(url, username, pwd)
        if result['code'] == 0:   # 正常登陆状态
            token = result['data']['token']
            fixconfig("token", token)  # 修改token的值为本次登录的token
            member_id = result['data']['member_id']
            fixconfig("member_id", str(member_id))  # 修改member_id的值为本次登录的,需要改一下字符類型
            company_id = result['data']['company_id']
            fixconfig("company_id", str(company_id))  # 修改company_id的值为本次登录的
        elif result['code'] == 1005102105:   # 此账号未注册，请检查输入的账号是否正确
            print(result['msg'])
        elif result['code'] == 1005001006:   # 账号未注册或密码错误
            print(result['msg'])
        else:
            print(coloring()['YELLOW']+'登陆报错……')
            # 打印日志到logs
            log = Log()
            log.debug('正常登录接口返回信息：%s' % result)

    def test_account_error_login(self):
        """用户名异常登陆，接口地址：/api/auth_center/v3/login"""
        pass

    def test_password_error_login(self):
        """密码异常登陆，接口地址：/api/auth_center/v3/login"""
        pass




from time import sleep
from ddt import ddt, data, unpack
from public.base import basetest
from public.common.datadriver import read_excel
from public.pages import loginpage


@ddt
class test(basetest.BaseTest):
    def _lg(self, username, password):
        """封装函数"""
        ngpage = loginpage.LoginPage(self.driver)
        ngpage.openurl()
        ngpage.send_username(username)
        self.assertEqual(username, 'zjn', msg='the username is not "zjn"')
        ngpage.send_password(password)
        self.assertEqual(password, int('111'), msg='the password is not "111"')
        ngpage.sub()
        sleep(2)

    @data(*read_excel('user_data.xlsx', 'Sheet1'))
    @unpack
    def test_login(self, flag, username, password):
        '''测试登录'''
        self._lg(username, password)

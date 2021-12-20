# from time import sleep
# from public.base import basetest
# from public.pages import loginpage, homepage, searchpage, geneinfopage
#
# '''
# 测试ng2 部分流程
# '''
#
#
# class test(basetest.BaseTest):
#     def test_kj(self):
#         '''测试基本功能'''
#         try:
#             lgpage = loginpage.LoginPage(self.driver)
#             hmpage = homepage.HomePage(self.driver)
#             scpage = searchpage.SearchPage(self.driver)
#
#             lgpage.openurl()
#             lgpage.send_username('zjn')
#             lgpage.send_password('111')
#             lgpage.sub()
#             sleep(2)
#
#             hmpage.search('p2rx7')
#             hmpage.searchbutton()
#
#             scpage.diseasetab()
#
#         except:
#             pass
#
#     def test_kj2(self):
#         '''测试基本功能2'''
#         try:
#             lgpage = loginpage.LoginPage(self.driver)
#             hmpage = homepage.HomePage(self.driver)
#
#             lgpage.openurl()
#             lgpage.send_username('zjn')
#             lgpage.send_password('111')
#             lgpage.sub()
#             sleep(2)
#
#             hmpage.search('p2rx7')
#             hmpage.searchbutton()
#         except:
#             pass
#
#     def test_kj3(self):
#         '''测试基本功能3'''
#         try:
#             lgpage = loginpage.LoginPage(self.driver)
#             hmpage = homepage.HomePage(self.driver)
#             scpage = searchpage.SearchPage(self.driver)
#
#             lgpage.openurl()
#             lgpage.send_username('zjn')
#             lgpage.send_password('111')
#             lgpage.sub()
#             sleep(2)
#
#             hmpage.search('p2rx7')
#             hmpage.searchbutton()
#
#             scpage.diseasetab()
#             scpage.varianttab()
#         except:
#             pass
#
#     def test_kj4(self):
#         '''测试基本功能4'''
#         try:
#             lgpage = loginpage.LoginPage(self.driver)
#             hmpage = homepage.HomePage(self.driver)
#             scpage = searchpage.SearchPage(self.driver)
#
#             lgpage.openurl()
#             lgpage.send_username('zjn')
#             lgpage.send_password('111')
#             lgpage.sub()
#             sleep(2)
#
#             hmpage.search('p2rx7')
#             hmpage.searchbutton()
#
#             scpage.diseasetab()
#             scpage.varianttab()
#         except:
#             pass

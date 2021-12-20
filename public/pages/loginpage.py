from selenium.webdriver.common.by import By
from public.base import basepage
from public.common.readconfig import ReadConfig, filepath

'''元素'''
# 登录
username_loc = (By.XPATH, '//*[@id="login-username-input"]')
password_loc = (By.XPATH, '//*[@id="login-password-input"]')
submit_loc = (By.XPATH, '//*[@id="inspire"]/div[2]/main/div/div/div/div/div/div[2]/button/div')


class LoginPage(basepage.Page):
    def openurl(self):
        """打开ng"""
        readconfig = ReadConfig(filepath)
        url = readconfig.getValue('openurl', "url")
        self.driver.open_url(url)

    # 输入用户名
    def send_username(self, value):
        self.driver.send_keys(username_loc, value)

    # 输入密码
    def send_password(self, value):
        self.driver.send_keys(password_loc, value)

    # 登录按钮
    def sub(self):
        self.driver.click(submit_loc)



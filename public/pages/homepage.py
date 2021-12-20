from selenium.webdriver.common.by import By

from public.base import basepage

# 搜索框一级
search_loc = (By.XPATH, ".//*[@id='warp-box']/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/input")
# 搜索按钮
searchbutton_loc = (By.XPATH, ".//*[@id='warp-box']/div[2]/div/div[2]/div[1]/div/div[1]/div[3]/i")
# EXamples
examples_loc = (By.XPATH, '//*[@id="warp-box"]/div[2]/div/div[2]/div[2]/span[2]')
# hotword
hotword_loc = (By.XPATH, '//*[@id="warp-box"]/div[2]/div/div[2]/div[3]/span[3]/span/span')
# target
target_loc = (By.XPATH, '//*[@id="warp-box"]/div[3]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/div/a')
# target跳转gene
targetgene_loc = (By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div/div/div[2]/span[2]/a')
# target跳转disease
targetdisease_loc = (
By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[4]/div/span/a/div')


class HomePage(basepage.Page):
    # 一级搜索框
    def search(self, info):
        self.driver.send_keys(search_loc, info)

    # 搜索按钮
    def searchbutton(self):
        self.driver.click(searchbutton_loc)

    # 点击EXamples
    def examples(self):
        self.driver.click(examples_loc)

    #点击 hotword
    def hotword(self):
        self.driver.click(hotword_loc)
    # 点击target
    def target(self):
        self.driver.click(target_loc)

    #点击 target跳转gene
    def targetgene(self):
        self.driver.click(targetgene_loc)

    # 点击target跳转disease
    def targetdisease(self):
        self.driver.click(targetdisease_loc)


# data = read_excel('user_data.xlsx', 'Sheet2')
#         ngpage.input(data[0][1])

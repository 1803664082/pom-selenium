from public.base import basepage
from selenium.webdriver.common.by import By

# search页搜索框
search1_loc = (By.XPATH, '//*[@id="app"]/div[3]/main/div/div/div[1]/div/div/div[1]/div/div[1]/div[1]/input')
# search页搜索按钮
searchbutton1_loc = (
By.XPATH, '//*[@id="app"]/div[3]/main/div/div/div[1]/div/div/div[1]/div/div[1]/div[3]/button/div/i')

# 收缩展开按钮
result_loc = (
By.XPATH, '//*[@id="app"]/div[3]/main/div/div/div[2]/div[1]/aside/nav/div/div/div/div/div[3]/button/div/i')

# varianttable
varianttab_loc = (By.CSS_SELECTOR, '.vgd-active .v-list__tile__title')
# genetable
genetab_loc = (By.CSS_SELECTOR, '.m-t-20:nth-child(3) .v-list__tile__title')
# diseasetable
diseasetab_loc = (By.CSS_SELECTOR, '.m-b-15 .v-list__tile__title')

# 测试用,点击genetable的第一个数据进行跳转
p2rx7_loc = (By.XPATH,
             '//*[@id="app"]/div[3]/main/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[3]/table/tbody/tr/td[1]/div/a/em/b')


class SearchPage(basepage.Page):

    # 对search页的搜索框进行输入
    def search1(self, value):
        self.driver.send_keys(search1_loc, value)

    # 点击search页的搜索按钮
    def searchbutton1(self):
        self.driver.click(searchbutton1_loc)

    # 点击展开搜索按钮
    def result_loc(self):
        self.driver.click(result_loc)

    # 点击并切换到variant_table页
    def varianttab(self):
        self.driver.click(varianttab_loc)

    # 点击并切换到gene_table页
    def genetab(self):
        self.driver.click(genetab_loc)

    # 点击并切换到disease_table页
    def diseasetab(self):
        self.driver.click(diseasetab_loc)

    # 测试自动化用数据
    def p2rx7(self):
        self.driver.click(p2rx7_loc)

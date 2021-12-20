from selenium.webdriver.common.by import By
from public.base import basepage

# MF
mf_loc = (By.CSS_SELECTOR, '#tab-0')
# BP
bp_loc = (By.CSS_SELECTOR, '#tab-1')
# CC
cc_loc = (By.CSS_SELECTOR, '#tab-2')
# KEGG
kegg_loc = (By.CSS_SELECTOR, '#tab-3')

# human
human_loc = (By.XPATH, ".//*[@id='tab-1']/span/div")
# dog
dog_loc = (By.XPATH, ".//*[@id='tab-2']/span/div")
# mouse
mouse_loc = (By.XPATH, ".//*[@id='tab-3']/span/div")
# humanprotein
humanprotein_loc = (By.XPATH, ".//*[@id='tab-4']/span/div")
# humantissuse
humantissuse_loc = (By.XPATH, ".//*[@id='tab-5']/span/div")
# humanbrain
humanbrain_loc = (By.XPATH, ".//*[@id='tab-6']/span/div")
# mousebrain
mousebrain_loc = (By.XPATH, ".//*[@id='tab-7']/span/div")
# omicsoft
omicsoft_loc = (By.XPATH, ".//*[@id='tab-8']/span/div")
# export导出
export_loc = (By.CSS_SELECTOR, ".v-toolbar__content")

# advanced_search button
advanced_search_loc = (By.CSS_SELECTOR, ".ml-5.v-btn.v-btn--small.theme--light")

# columns
columns_loc = (By.CSS_SELECTOR, '.query.px-3.v-btn.v-btn--small.theme--light')

# 切换到heatmap
geneheatmap_loc = (By.XPATH, ".//*[@id='GeneAssociatedDiseases']/div[2]/div/div[2]/div[1]/div/div/div[2]/a/div")
# 切换bubbles
genebubbles_loc = (By.XPATH, ".//*[@id='GeneAssociatedDiseases']/div[2]/div/div[2]/div[1]/div/div/div[3]/a")
# 切换table
genetable_loc = (By.XPATH, ".//*[@id='GeneAssociatedDiseases']/div[2]/div/div[2]/div[1]/div/div/div[4]/a/div")


class GeneInfoPage(basepage.Page):
    def mf(self):
        '''点击mf'''
        self.driver.click(mf_loc)

    def bp(self):
        '''点击bp'''
        self.driver.click(bp_loc)

    def cc(self):
        '''点击cc'''
        self.driver.click(cc_loc)

    def kegg(self):
        '''点击kegg'''
        self.driver.click(kegg_loc)
        self.driver.Scrollbar(kegg_loc)

    def human(self):
        '''点击human'''
        self.driver.click(human_loc)

    def dog(self):
        '''点击dog'''
        self.driver.click(dog_loc)

    def mouse(self):
        '''点击mouse'''
        self.driver.click(mouse_loc)
        self.driver.Scrollbar(mouse_loc)

    def humanprotein(self):
        '''点击humanprotein'''
        self.driver.click(humanprotein_loc)

    def humantissuse(self):
        '''点击humantissuse'''
        self.driver.click(humantissuse_loc)

    def humanbrain(self):
        '''点击humanbrain'''
        self.driver.click(humanbrain_loc)

    def mousebrain(self):
        '''点击mousebrain'''
        self.driver.click(mousebrain_loc)
        self.driver.Scrollbar(mousebrain_loc)

    def omicsoft(self):
        '''点击omicsoft'''
        self.driver.click(omicsoft_loc)

    def export(self):
        self.driver.click(export_loc)

    def advanced_search(self):
        self.driver.click(advanced_search_loc)

    def columns(self):
        self.driver.click(columns_loc)

    def heatmap(self):
        self.driver.click(geneheatmap_loc)
        self.driver.Scrollbar(geneheatmap_loc)

    def bubbles(self):
        self.driver.click(genebubbles_loc)

    def table(self):
        self.driver.click(genetable_loc)

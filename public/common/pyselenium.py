import sys
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from public.common.log import Log
from selenium.webdriver import ChromeOptions
from public.common.readconfig import ReadConfig, filepath

logger = Log()
success = "SUCCESS>>>>"
fail = "FAIL>>>>"
t1 = time.time()


class PySelenium(object):
    read_config = ReadConfig(filepath)
    browser_type = read_config.getValue('driver-type', 'driver')

    def __init__(self, browser_type=browser_type):
        if browser_type == "firefox" or browser_type == "Firefox":
            driver = webdriver.Firefox()
        elif browser_type == "chrome" or browser_type == "Chrome":
            option = ChromeOptions()
            option.add_argument("--headless")
            # driver = webdriver.Chrome(options=option) # 支持浏览器以无头模式启动,可提高30%效率
            driver = webdriver.Chrome()
        elif browser_type == "edge":
            driver = webdriver.Edge()
        else:
            driver = webdriver.Chrome()
        try:
            self.driver = driver
            self.log_info(
                "{0} Start a new browser: {1}, Spend {2} seconds".format(success, browser_type, time.time() - t1))
        except Exception:
            raise NameError("Not found {0} browser,You can enter 'edge','firefoxf','chrome'.".format(browser_type))

    # 日志级别封装
    def log_debug(self, msg):
        """debug"""
        logger.debug(msg)

    def log_info(self, msg):
        """info"""
        logger.info(msg)

    def log_warning(self, msg):
        """warning"""
        logger.warning(msg)

    def log_error(self, msg):
        """error"""
        logger.error(msg)

    def wait(self, secs):
        """ 隐式等待 """
        self.driver.implicitly_wait(secs)
        self.log_info("{0} Set the browser implicit wait to: {1} seconds, Spend {2} seconds".format(success, secs,
                                                                                                    time.time() - t1))

    def open_url(self, url):
        """ 访问URL """
        try:
            self.driver.get(url)
            self.log_info("{0} Navigated to {1}, Spend {2} seconds".format(success, url, time.time() - t1))
        except Exception:
            self.log_error("{0} Unable to load {1}, Spend {2} seconds".format(fail, url, time.time() - t1))
            raise

    def locator(self, loc) -> WebElement:
        """ 单元素定位 """
        try:
            self.log_info("{0} The current element is positioned as {1}".format(success, loc))

            return self.driver.find_element(*loc)
        except Exception:
            self.log_error(
                "{0} No related operation was found {1} ,Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.".format(
                    fail, loc))

    def locators(self, loc) -> [WebElement]:
        """ 多元素定位 """
        return self.driver.find_elements(*loc)

    def get_attribute(self, loc, attribute):
        """ 获取元素属性 """
        el = self.locator(loc)
        return el.get_attribute(attribute)

    def get_text(self, loc):
        """ 获取text """
        el = self.locator(loc)
        return el.text

    def get_title(self):
        """ 获取title """
        self.log_info("{0} Get current title , Spend {1} seconds".format(success, time.time() - t1))
        return self.driver.title

    def send_keys(self, loc, value):
        """ 输入 """
        self.locator(loc).send_keys(value)
        self.log_info(
            "{0} Element {1}, input parameter <{2}> , Spend {3} seconds".format(success, loc, value, time.time() - t1))

    def clear(self, loc):
        """ 清除文本框内容 """
        el = self.locator(loc)
        el.clear()

    def get_value(self, loc):
        """ 获取文本值 """
        self.log_info("{0} Get text values{1}  , Spend {2} seconds".format(success, loc, time.time() - t1))
        return self.locator(loc).text

    def click(self, loc):
        """ 单击 """
        try:
            self.locator(loc).click()
            self.log_info("{0} Clicked element: {1}, Spend {2} seconds".format(success, loc, time.time() - t1))
        except Exception:
            self.log_error("{0} Unable to click element: {1}, Spend {2} seconds".format(fail, loc, time.time() - t1))

    def right_click(self, loc):
        """ 右键操作 """
        try:
            el = self.locator(loc)
            ActionChains(self.driver).context_click(el).perform()
            self.log_info("{0} Right click element: <{1}>, Spend {2} seconds".format(success, loc, time.time() - t1))
        except Exception:
            self.log_error(
                "{0} Unable to right click element: <{1}>, Spend {2} seconds".format(fail, loc, time.time() - t1))
            raise

    def Scrollbar(self, target):
        """
        操作滚动条的方法
        target是元素位置
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def double_click(self, loc):
        """
         双击元素
        """
        t1 = time.time()
        try:
            el = self.locator(loc)
            ActionChains(self.driver).double_click(el).perform()
            self.log_info("{0} Double click element: <{1}>, Spend {2} seconds".format(success, loc, time.time() - t1))
        except Exception:
            self.log_error(
                "{0} Unable to double click element: <{1}>, Spend {2} seconds".format(fail, loc, time.time() - t1))
            raise

    def hover(self, loc):
        """ 鼠标悬停 """
        try:
            el = self.locator(loc)
            ActionChains(self.driver).move_to_element(el).perform()
            self.log_info("{0} Move to element: <{1}>, Spend {2} seconds".format(success, loc, time.time() - t1))
        except Exception:
            self.log_error("{0} unable move to element: <{1}>, Spend {2} seconds".format(fail, loc, time.time() - t1))
            raise

    def drag_and_drop(self, el_key, ta_key):
        """ 拖拽 从一个元素拖到另外一个元素 """
        el = self.locator(el_key)
        target = self.locator(ta_key)
        ActionChains(self.driver).drag_and_drop(el, target).perform()

    def choice_select(self, loc, value):
        """ 下拉框 """
        sel = Select(self.locator(loc))
        sel.select_by_value(value)

    def goto_frame(self, frame_name):
        """ 进框架 """
        try:
            self.driver.switch_to.frame(frame_name)
            self.log_info("{0} Enter {1} frame  , Spend {2} seconds".format(success, frame_name, time.time() - t1))
        except Exception:
            self.log_error(
                "{0} No frame with name {1} found  , Spend {2} seconds".format(fail, frame_name, time.time() - t1))

    def quit_frame(self):
        """ 出框架 """
        self.driver.switch_to.default_content()

    def submit(self, loc):
        """ 提交事件 """
        el = self.locator(loc)
        el.submit()

    def F5(self):
        """ 刷新 """
        self.driver.refresh()
        self.log_info("{0} Refresh the browser with 'F5', Spend {1} seconds".format(success, time.time() - t1))

    def js(self, script):
        """ 执行js """
        self.driver.execute_script(script)

    def back(self, breakCount):
        """ 后退 """
        sum = 0
        while sum > breakCount:
            self.driver.back()
            sum += 1

    def close(self):
        """ 关闭当前页签 """
        self.log_info("{0} Close the current TAB, Spend {1} seconds".format(success, time.time() - t1))
        return self.driver.close()

    def max_window(self):
        """ 最大化窗口 """
        # self.driver.maximize_window()

        self.driver.maximize_window()
        self.log_info("{0} Set browser window maximized, Spend {1} seconds".format(success, time.time() - t1))

    def set_windows(self, wide, high):
        """ 设置窗口大小 """
        self.driver.set_window_size(wide, high)
        self.log_info("{0} Set browser window wide: {1},high: {2}, Spend {3} seconds".format(success, wide, high,
                                                                                             time.time() - t1))

    def switch_to(self, index):
        """-1 切换到新窗口  -2切换到倒数第二个打开的窗口   0切换到最开始打开的窗口"""
        hand = self.driver.window_handles
        self.driver.switch_to.window(hand[index])

    def to_frame(self, loc):
        """ 窗口切换 """
        el = self.locator(loc)
        self.driver.switch_to.frame(el)

    def alert_accept(self):
        """ 对话框确认操作 """
        self.driver.switch_to.alert.accept()

    def alert_dismiss(self):
        """ 对话框取消操作 """
        self.driver.switch_to.alert.dismiss()

    def screenshot(self, picture_path):
        """ 截图 """
        self.driver.save_screenshot(picture_path)  # self.screenshot(str(time.time()) + ".png")

    def quit(self):
        """ 退出浏览器 """
        time.sleep(2)
        self.driver.close()
        self.driver.quit()
        self.log_info("{0} Close the driver and exit the current browser".format(success))


if __name__ == '__main__':
    driver = PySelenium("chrome")

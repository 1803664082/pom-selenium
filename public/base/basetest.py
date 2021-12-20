import unittest
from public.common import pyselenium
from public.common.log import Log
from public.common.readconfig import ReadConfig, filepath


class BaseTest(unittest.TestCase):
    """
    所有测试类的基类
    """
    def setUp(self):
        self.logger = Log()
        read_config = ReadConfig(filepath)
        driver_type = read_config.getValue('driver-type', 'driver')
        self.logger.info('----------------------- START -----------------------')
        self.driver = pyselenium.PySelenium(driver_type)
        self.driver.max_window()

    def tearDown(self):
        self.driver.quit()
        self.logger.info('-----------------------  End  -----------------------')

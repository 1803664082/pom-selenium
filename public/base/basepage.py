class Page(object):
    """
    所有页面对象的基类
    """

    def __init__(self, selenium_driver):
        self.driver = selenium_driver

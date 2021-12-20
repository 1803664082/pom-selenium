import unittest
import HTMLTestRunner
import time
from public.common.readconfig import ReadConfig, filepath


def run():
    test_dir = './testcase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test*.py')
    now = time.strftime('%Y-%m-%d_%H_%M_%S')

    read_config = ReadConfig(filepath)
    report_path = read_config.getValue('projectConfig', 'report_path')
    report_name = report_path + '\\' + 'TestResult' + now + '.html'
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f)
        runner.run(suite)
    time.sleep(3)

    # # 定义一个单元测试容器
    # testsuite = unittest.TestSuite()
    # # 将测试用例加入到容器
    # testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test))


if __name__ == '__main__':
    run()

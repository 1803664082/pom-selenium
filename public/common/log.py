import logging
import sys
import time
import os
from public.common.readconfig import ReadConfig, filepath

read_config = ReadConfig(filepath)
log_path = read_config.getValue('projectConfig', 'log_path')


class Log:
    def __init__(self):
        self.logname = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))

    def __printconsole(self, level, message):
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.logname, 'w', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(sh)

        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(sh)
        logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__printconsole('debug', message)

    def info(self, message):
        self.__printconsole('info', message)

    def warning(self, message):
        self.__printconsole('warning', message)

    def error(self, message):
        self.__printconsole('error', message)

import configparser
import codecs
import os

filepath = os.path.abspath(r"config/config.ini")

'''
获取配置文件数据
'''


class ReadConfig:
    def __init__(self, filepath):
        fd = open(filepath)
        data = fd.read()
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            files = codecs.open(filepath, "w")
            files.write(data)
            files.close()
        fd.close()
        self.cf = configparser.ConfigParser()
        self.cf.read(filepath)

    def getValue(self, env, name):
        return self.cf.get(env, name)


if __name__ == '__main__':
    test = ReadConfig('D:\library\selenium_pom\config\config.ini')
    t = test.getValue('openurl', "url")
    print(t)

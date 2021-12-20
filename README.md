# pom-selenium
[前置配置]
浏览器:chrome 96.0.4664.93
浏览器驱动:需下载对应浏览器版本的驱动程序并配置环境变量,一般放在python根目录下;详细内容请访问http://npm.taobao.org/mirrors/chromedriver/
selenium:3.141.0   pip install selenium=3.141.0   pip list
python:3.9.6

[项目目录说明]
config
    --config.ini    测试地址与输出文件路径

data
    --testdata  测试数据的存放路径

public
    --base
        ---basepage     页面对象的基类,需继承
        ---basetest     测试用例的基类,需继承
    --common
        ---datadriver   数据驱动类,封装了读取csv,json,excel文件的方法
        ---log          logger类,封装了log相关的方法
        ---pyselenium   selenium二次封装,同时封装了浏览器驱动
        ---readconfig   封装了读取config文件的方法
    --pages     页面对象路径

report
    --image     存放截图路径
    --log       存放log路径,log不会主动清空,需手动清空
    --testreport    存放测试报告路径
testcase        存放测试用例路径

HTMLTestRunner.py       生成测试报告插件

Run.py      启动类,可一次性启动testcase/test* 的所有用例

#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import unittest
import HTMLTestRunner
import time
def creatsuite():
    testunit=unittest.TestSuite()
    #定义测试文件查找的目录
    test_dir = r'C:\Python27\Projects\Test126'
    #定义discover 方法的参数
    discover=unittest.defaultTestLoader.discover(test_dir,
                                                pattern ='test*.py',
                                                top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print testunit
    return testunit

now = time.strftime("%Y-%m-%d %H_%M_%S")
#定义个报告存放路径
filename = r'C:\Python27\Projects\Test126_report\T'
filename = filename + now + 'result.html'
fp = file(filename, 'wb')
#定义测试报告
runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'百度搜索测试报告',
    description=u'用例执行情况：')

if __name__ == '__main__':
    #runner =unittest.TextTestRunner()
    alltestnames = creatsuite()
    runner.run(alltestnames)
    fp.close()

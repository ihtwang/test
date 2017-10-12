#coding=utf-8
import unittest
def creatsuite():
    testunit=unittest.TestSuite()
    #定义测试文件查找的目录
    test_dir='C:\\Python27\\Projects\\Test'
    #定义discover 方法的参数
    discover=unittest.defaultTestLoader.discover(test_dir,
                                                pattern ='test3*.py',
                                                top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            print '*****111'
            print testunit
            testunit.addTests(test_case)
            print testunit
            print '***'
    return testunit
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    alltestnames = creatsuite()
    runner.run(alltestnames)
    #runner.run(testunit)
    

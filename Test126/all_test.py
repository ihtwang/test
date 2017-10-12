#coding=utf-8
import unittest
#加载测试文件
#import test_login
#import test_send
#import test_search
import test_del

# 构造测试集
suite = unittest.TestSuite()
#suite.addTest(test_login.TestLogin("test_null"))
#suite.addTest(test_login.TestLogin("test_pawd_null"))
#suite.addTest(test_login.TestLogin("test_user_null"))
#suite.addTest(test_login.TestLogin("test_error"))
#suite.addTest(test_login.TestLogin("test_login"))
#suite.addTest(test_send.TestSendMail("test_send_mail"))
#suite.addTest(test_send.TestSendMail("test_send_mail2"))
#suite.addTest(test_send.TestSendMail("test_send_mail3"))
#suite.addTest(test_send.TestSendMail("test_send_mail4"))
#suite.addTest(test_search.TestSearchMail("test_search_mail1"))
suite.addTest(test_del.TestDelMail("test_del_mail1"))

if __name__ == '__main__':
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

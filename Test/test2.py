#coding=utf-8
from count import Count
import unittest
class TestAdd(unittest.TestCase):
    def setUp(self):
        pass
    #测试整数相加
    def test_add(self):
        self.j = Count(2,3)
        self.add = self.j.add()
        self.assertEqual(self.add,5)
    #测试小数相加
    def test_add2(self):
        self.j = Count(2.3,4.2)
        self.add = self.j.add()
        self.assertEqual(self.add,6.5)
    #测试字符串相加
    def test_add3(self):
        self.j = Count("hello"," world")
        self.add = self.j.add()
        self.assertEqual(self.add,"hello world")
    def tearDown(self):
        pass
    
class TestSubtraction(unittest.TestCase):
    def setUp(self):
        pass
    #测试整数相减
    def test_subtraction(self):
        self.j = Count(2,3)
        self.sub = self.j.subtraction()
        self.assertEqual(self.sub,-1)
        #测试小数相减
    def test_subtraction2(self):
        self.j = Count(4.2,2.2)
        self.sub = self.j.subtraction()
        self.assertEqual(self.sub,2)
    def tearDown(self):
        pass
if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_add"))
    suite.addTest(TestAdd("test_add2"))
    suite.addTest(TestAdd("test_add3"))
    
    suite.addTest(TestSubtraction("test_subtraction"))
    suite.addTest(TestSubtraction("test_subtraction2"))
    
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

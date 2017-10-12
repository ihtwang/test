# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class se_rc(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://www.baidu.com/")
        self.selenium.start()
    
    def test_se_rc(self):
        sel = self.selenium
        sel.open("/")
        sel.type("id=kw", "selenium")
        sel.click("id=su")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

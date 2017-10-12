# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestLogon(unittest.TestCase):
    def setUp(self):

        # 配置文件地址
        profile_directory = r"C:\Users\IBM_ADMIN\AppData\Roaming\Mozilla\Firefox\Profiles\3fyggsfu.default"
 
        # 加载配置配置
        profile = webdriver.FirefoxProfile(profile_directory)
        # 启动浏览器配置
        self.driver = webdriver.Firefox(profile)
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.126.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_logon(self):
        driver = self.driver
        driver.get(self.base_url + "/")

        #driver.find_element_by_id("auto-id-1505045564984").clear()
        #driver.find_element_by_id("auto-id-1505045564984").send_keys("Wzj1234abcd20")

        frame = driver.find_element_by_id('x-URS-iframe')
        driver.switch_to_frame(frame)
        # XXXX替换为你的用名和密码
        #driver.find_element_by_css_selector("form input[name='email']").clear()
        #driver.find_element_by_css_selector("form input[name='email']").send_keys("iht_wang")
        #time.sleep(1)
        #driver.find_element_by_css_selector("form input[name='password']").clear()
        #driver.find_element_by_css_selector("form input[name='password']").send_keys("Wzj1234abcd20")
        #time.sleep(1)
        prompt_info = u"帐号或密码错误"
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("iht_wang1")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("Wzj1234abcd20")
        driver.find_element_by_id("dologin").click()
        time.sleep(10)


         #获取断言信息进行断言
        #text = driver.find_element_by_xpath("//div[@class='error-tt']/p").text
        text = driver.find_element_by_xpath("//div[@class='ferrorhead']").text
        print u"****" + text
        self.assertEqual(text,prompt_info)
        
        #driver.switch_to_default_content()
        #text_ = driver.find_element_by_xpath("//*[@id='spnUid']").text
        #text_ = driver.find_element_by_css_selector('#spnUid').text
        #text_ = driver.find_element_by_id("spnUid").text
        
        
        #print u"****" + text_
        #self.assertEqual("iht_wang@126.com", text_)
        #time.sleep(10)
        #print u"准备退出。。。"
        #driver.find_element_by_link_text(u"退出").click()
        #print u"退出了"
        #time.sleep(15)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        #self.driver.quit()
        print u"准备关闭浏览器。。。"
        time.sleep(15)
        self.driver.close()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

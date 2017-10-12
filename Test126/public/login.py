#coding=utf-8
import time
#登录
def login(self):
    driver = self.driver
    frame = driver.find_element_by_id('x-URS-iframe')
    driver.switch_to_frame(frame)
    #driver.find_element_by_id("idInput").clear()
    #driver.find_element_by_id("idInput").send_keys(username)
    #driver.find_element_by_id("pwdInput").clear()
    #driver.find_element_by_id("pwdInput").send_keys(password)
    #driver.find_element_by_id("loginBtn").click()
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(self.username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(self.password)
    
    #print 'Waiting for about 8 seconds please...'
    time.sleep(2)
    driver.find_element_by_id("dologin").click()

    
    
#退出
def logout(self):
    driver = self.driver
    driver.find_element_by_link_text(u"退出").click()

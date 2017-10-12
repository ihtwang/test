#coding=utf-8
from selenium import webdriver
import unittest, time
from public import login
import xml.dom.minidom
import SendKeys
#引入Keys 模块
from selenium.webdriver.common.keys import Keys

#打开xml 文档
dom = xml.dom.minidom.parse(r'C:\Python27\Projects\Test126_data\login.xml')
#得到文档元素对象
root = dom.documentElement

class TestSearchMail(unittest.TestCase):
    def setUp(self):
        # 配置文件地址
        profile_directory = r"C:\Users\IBM_ADMIN\AppData\Roaming\Mozilla\Firefox\Profiles\3fyggsfu.default"
 
        # 加载配置配置
        profile = webdriver.FirefoxProfile(profile_directory)
        # 启动浏览器配置
        self.driver = webdriver.Firefox(profile)
        #self.driver = webdriver.Firefox()
        # set window size
        #time.sleep(10)
        self.driver.set_window_size(480, 320)
        time.sleep(5)
        print self.driver.get_window_size()

        #maximize window
        self.driver.maximize_window()
        print self.driver.get_window_size()
        
        self.driver.implicitly_wait(30)
        logins = root.getElementsByTagName('url')
        self.base_url=logins[0].firstChild.data
        logins = root.getElementsByTagName('user_pawd')
        #获得user_pawd 标签的username、passwrod 属性值
        self.username=logins[0].getAttribute("username")
        self.password=logins[0].getAttribute("password")
        self.verificationErrors = []
        #只填写收件人发送邮件
    def test_search_mail1(self):
        driver = self.driver
        driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        
        #登录
        login.login(self)

        driver.switch_to_default_content()

        #搜索邮件
        driver.find_element_by_xpath("//input[@class='nui-ipt-input' and \
                                    @type='text']").send_keys(u'小明')
        time.sleep(5)
        driver.find_element_by_xpath("//input[@class='nui-ipt-input' and \
                                    @type='text']").send_keys(Keys.ENTER)

        #断言搜索邮件标签页面
        time.sleep(5)
        text= driver.find_element_by_xpath("//div[@id='dvMultiTab']/ul\
                                            /li[8]/div[3]").text
        time.sleep(3)
        self.assertEqual(text,u'搜索邮件')

        print u"准备退出..."
        login.logout(self)
        print u"退出了..."

        
    def tearDown(self):
        print u"准备关闭浏览器..."
        time.sleep(5)
        #self.driver.close()
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    unittest.main()

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

class TestDelMail(unittest.TestCase):
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
    def test_del_mail1(self):
        driver = self.driver
        driver.get(self.base_url)
        #self.driver.implicitly_wait(30)
        
        #登录
        login.login(self)

        driver.switch_to_default_content()
        time.sleep(5)
        driver.find_element_by_class_name('nui-tree-item-text').click()
        #driver.find_element_by_class_name(\
        #    'nui-tabs-item-text nui-fNoSelect').click()
        #driver.find_element_by_xpath("//span[@calss='nui-tree-item-text' and \
        #                            @title=u'收件箱']").click()
        print u"点击了收件箱"
        time.sleep(5)
        
        driver.find_elements_by_xpath("//span[@class='nui-chk-symbol']\
                                    /b").pop(1).click()
        time.sleep(3)
        try:
            spans = driver.find_elements_by_tag_name('span')
            for s in spans:
                #print s.text
                if s.text == u'删 除':
                    s.click()
                    print u"点击删除"
                    break
        except:
            #print u"没找到删除键"
            pass
            
        #断言是否已删除
        time.sleep(5)
        text = driver.find_element_by_css_selector(\
            "span.nui-tips-text > a").text
        self.assertEqual(text,u'已删除')
        #退出

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

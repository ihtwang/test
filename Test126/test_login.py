#coding=utf-8
from selenium import webdriver
import unittest, time
#导入login 文件
from public import login
import xml.dom.minidom

#打开xml 文档
dom = xml.dom.minidom.parse(r'C:\Python27\Projects\Test126_data\login.xml')
#得到文档元素对象
root = dom.documentElement

class TestLogin(unittest.TestCase):
    def setUp(self):
        # 配置文件地址
        profile_directory = r"C:\Users\IBM_ADMIN\AppData\Roaming\Mozilla\Firefox\Profiles\3fyggsfu.default"
 
        # 加载配置配置
        profile = webdriver.FirefoxProfile(profile_directory)
        # 启动浏览器配置
        self.driver = webdriver.Firefox(profile)
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        logins = root.getElementsByTagName('url')
        self.base_url = logins[0].firstChild.data
        #self.base_url = "http://www.126.com/"
        self.verificationErrors = []

    #用户名、密码为空
    def test_null(self):
        driver = self.driver
        driver.get(self.base_url)
        logins = root.getElementsByTagName('null')
        #获得null 标签的username、passwrod 属性值
        self.username=logins[0].getAttribute("username")
        self.password=logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        #登录
        login.login(self)

        time.sleep(10)
        
        
        #获取断言信息进行断言
        #text = driver.find_element_by_xpath("//div[@class='error-tt']/p").text
        text = driver.find_element_by_xpath("//div[@class='ferrorhead']").text
        print "username=" + self.username + ";password=" + self.password
        print text
        self.assertEqual(text,prompt_info)
        
    #输入用户名、密码为空
    def test_pawd_null(self):
        driver = self.driver
        driver.get(self.base_url)
        logins = root.getElementsByTagName('pawd_null')
        #获得null 标签的username、passwrod 属性值
        self.username=logins[0].getAttribute("username")
        self.password=logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        #登录
        login.login(self)
       
        
        #获取断言信息进行断言
        text = driver.find_element_by_xpath("//div[@class='ferrorhead']").text
        print "username=" + self.username + ";password=" + self.password
        print text
        self.assertEqual(text,prompt_info)
        
        #用户名为空，只输入密码
    def test_user_null(self):
        driver = self.driver
        driver.get(self.base_url)
        logins = root.getElementsByTagName('user_null')
        #获得null 标签的username、passwrod 属性值
        self.username=logins[0].getAttribute("username")
        self.password=logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        #登录
        login.login(self)
      
        
        #获取断言信息进行断言
        text = driver.find_element_by_xpath("//div[@class='ferrorhead']").text
        print "username=" + self.username + ";password=" + self.password
        print text
        self.assertEqual(text,prompt_info)
        
        #用户名密码错误
    def test_error(self):
        driver = self.driver
        driver.get(self.base_url)
        logins = root.getElementsByTagName('error')
        #获得null 标签的username、passwrod 属性值
        self.username=logins[0].getAttribute("username")
        self.password=logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data


        #登录
        login.login(self)
        
        verification_codes = root.getElementsByTagName('verification_code')
        verification_code = verification_codes[0].firstChild.data
        verification_results = root.getElementsByTagName('verification_result')
        verification_ok = verification_results[0].firstChild.data
        verification_fail = verification_results[1].firstChild.data
        
        #获取断言信息进行断言
        text = driver.find_element_by_xpath("//div[@class='ferrorhead']").text
        print "username=" + self.username + ";password=" + self.password
        print text
        print "****" + verification_code + "*****"
        if text == verification_code:
            print 'Vefify please...'
            time.sleep(8)
            text = driver.find_element_by_xpath("//div[@class='ncpt_hint_txt']/font").text

            #text = driver.find_element_by_xpath("//div[@class='ferrorhead']").text
            #print text
            if text == verification_ok:
                print text
                #self.assertEqual(text,verification_ok)
                print 'Will click on ok after 5 seconds... '
                time.sleep(5)
                driver.find_element_by_id("dologin").click()
                time.sleep(10)
                text = driver.find_element_by_xpath("//div[@class='ferrorhead']").text
                print text
                self.assertEqual(text,prompt_info)
                
            elif text == verification_fail:
                print text
                self.assertEqual(text,verification_fail)
            else:
                text = driver.find_element_by_xpath("//div[@class='ferrorhead']").text
                print text
                self.assertEqual(text,prompt_info)

        
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        logins = root.getElementsByTagName('user_pawd')
        #获得user_pawd 标签的username、passwrod 属性值
        self.username=logins[0].getAttribute("username")
        self.password=logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        
        
        #登录
        login.login(self)
        
        
        #获取断言信息进行断言
        driver.switch_to_default_content()
        text = driver.find_element_by_id("spnUid").text
        print "username=" + self.username + ";password=" + self.password
        print text
            
        self.assertEqual(text,prompt_info)
        time.sleep(10)
        
        print u"准备退出..."
        #调用退出函数
        login.logout(self)
        print u"退出了"
        time.sleep(15)
        
    def tearDown(self):
        print u"准备关闭浏览器..."
        time.sleep(5)
        #self.driver.quit()
        self.driver.close()
        time.sleep(5)
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()

#coding=utf-8
from selenium import webdriver
import unittest, time
from public import login
import xml.dom.minidom
import SendKeys

#打开xml 文档
dom = xml.dom.minidom.parse(r'C:\Python27\Projects\Test126_data\login.xml')
#得到文档元素对象
root = dom.documentElement

class TestSendMail(unittest.TestCase):
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
    def test_send_mail(self):
        driver = self.driver
        driver.get(self.base_url)
        self.driver.implicitly_wait(30)

        #logins = root.getElementsByTagName('user_pawd')
        #获得user_pawd 标签的username、passwrod 属性值
        #username=logins[0].getAttribute("username")
        #password=logins[0].getAttribute("password")
        #prompt_info = logins[0].firstChild.data
        
        
        #登录
        login.login(self)
        #login.login(self,username,password)
        #login.login(self,"testingwtb","a123456")
        driver.switch_to_default_content()
        #写信
        time.sleep(10)
        driver.find_element_by_css_selector("#_mail_component_70_70 > span.oz0").click()
        time.sleep(10)
        #填写收件人
        driver.find_element_by_xpath("//*[@class='bz0']/div[2]/\
                                     div[1]/input").\
            send_keys(self.username + '@126.com;')
        #driver.find_element_by_id("//*[@class='bz0']/div[2]/div/input").send_keys(Keys.ENTER)
        #html/body/div[7]/table/tbody/tr/td/span/strong[1]
        #html/body/div[7]/table/tbody/tr/td/span/strong[1]
        #发送邮件
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]\
                                     /header/div[1]/div[1]/div[1]\
                                     /span[2]").click()
        #driver.find_element_by_xpath("//*[@id='_mail_button_2_182']/span[2]").click()
        #driver.find_element_by_xpath("//*[@id='_mail_button_9_208']/span[2]").click()
        #driver.find_element_by_xpath("//span[contains(text(),'发送') and @class='nui-btn-text']").click()
        time.sleep(10)
        driver.find_element_by_xpath("//*[@class='nui-msgbox-ft-btns']/div/span").click()
        #断言发送结果
        time.sleep(10)
        text = driver.find_element_by_class_name('tK1').text
        self.assertEqual(text,u'发送成功可用手机接收回复')
        print u"准备退出..."
        login.logout(self)
        print u"退出了..."


    #填写收件人、主题发送邮件
    def test_send_mail2(self):
        driver = self.driver
        driver.get(self.base_url)
        #登录
        login.login(self)
        #login.login(self,"testingwtb","a123456")
        driver.switch_to_default_content()
        #写信
        #driver.find_element_by_css_selector("#_mail_component_47_47 > span.oz0").click()
        time.sleep(10)
        driver.find_element_by_css_selector("#_mail_component_70_70 > span.oz0").\
                                                                    click()
        time.sleep(10)
        #填写收件人和主题
        driver.find_element_by_xpath("//*[@class='bz0']/div[2]/div[1]/input")\
            .send_keys(self.username + '@126.com;')

        #填写收件人和主题
        #driver.find_element_by_xpath("//*[@class='bz0']/div[2]
        #                /div/input").send_keys('testingwtb@126.com')
        #driver.find_element_by_xpath("//input[@class='nui-ipt-input' and
        #                            @type='text' and @maxlength='256']").\
        #    send_keys(u'给小明的信')
        driver.find_element_by_xpath("//input[@class='nui-ipt-input'\
                                     and @type='text'\
                                     and @maxlength='256']").\
            send_keys(u'给iht的信')                                    
        #发送邮件
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]\
                                     /header/div[1]/div[1]/div[1]\
                                     /span[2]").click()

        #driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/header
        #/div/div/div/span[2]").click()
        #断言发送结果
        time.sleep(10)
        text = driver.find_element_by_class_name('tK1').text
        self.assertEqual(text,u'发送成功可用手机接收回复')
        print u"准备退出..."
        login.logout(self)
        print u"退出了..."
        #text = driver.find_element_by_class_name('tK1').text
        #self.assertEqual(text,u'发送成功')
        #login.logout(self)
        
    #填写收件人、主题和附件发送邮件
    def test_send_mail3(self):
        driver = self.driver
        driver.get(self.base_url)

        #登录
        login.login(self)

        driver.switch_to_default_content()
        #写信
        #driver.find_element_by_css_selector("#_mail_component_47_47 > span.oz0").click()
        time.sleep(10)
        driver.find_element_by_css_selector("#_mail_component_70_70 >\
                                            span.oz0").click()
        time.sleep(10)
        #填写收件人和主题
        driver.find_element_by_xpath("//*[@class='bz0']/div[2]/div[1]/input")\
            .send_keys(self.username + '@126.com;')
        time.sleep(5)
        driver.find_element_by_xpath("//input[@class='nui-ipt-input'\
                                     and @type='text'\
                                     and @maxlength='256']").\
            send_keys(u'给iht的信')   
        time.sleep(10)
                             
        #上传附件
        print u"准备上传附件"
        #driver.find_element_by_class_name("O0").send_keys(
        #    r'C:\Python27\python.exe')

        driver.find_element_by_class_name("by0").click()
        time.sleep(2)

        # SendKeys
        SendKeys.SendKeys(r'C:\Python27\python.exe')  # 发送文件地址
        time.sleep(2)
        SendKeys.SendKeys("{ENTER}") # 发送回车键


        
        print u"准备发送邮件"
        

        #发送邮件
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]\
                                     /header/div[1]/div[1]/div[1]\
                                     /span[2]").click()

        #断言发送结果
        time.sleep(10)
        text = driver.find_element_by_class_name('tK1').text
        self.assertEqual(text,u'发送成功可用手机接收回复')
        print u"准备退出..."
        login.logout(self)
        print u"退出了..."

    #填写收件人、主题和正文发送邮件
    def test_send_mail4(self):
        driver = self.driver
        driver.get(self.base_url)

        #登录
        login.login(self)

        driver.switch_to_default_content()
        #写信
        time.sleep(10)
        driver.find_element_by_css_selector("#_mail_component_70_70 >\
                                            span.oz0").click()
        time.sleep(10)
        #填写收件人和主题
        driver.find_element_by_xpath("//*[@class='bz0']/div[2]/div[1]/input")\
            .send_keys(self.username + '@126.com;')
        time.sleep(5)
        driver.find_element_by_xpath("//input[@class='nui-ipt-input'\
                                     and @type='text'\
                                     and @maxlength='256']").\
            send_keys(u'给iht的信')   
        time.sleep(10)

                             
        #定位富文本表单
        class_name = driver.find_element_by_class_name('APP-editor-iframe')
        driver.switch_to_frame(class_name)
        #编写邮件正文
        driver.find_element_by_tag_name('body').send_keys(u'你好，\
                                                          小明好久不见。')

        time.sleep(10)
        print u"准备发送邮件"
        #发送邮件
        driver.switch_to_default_content()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]\
                                     /header/div[1]/div[1]/div[1]\
                                     /span[2]").click()
        
        time.sleep(10)
        #断言发送结果
        text = driver.find_element_by_class_name('tK1').text
        self.assertEqual(text,u'发送成功可用手机接收回复')
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

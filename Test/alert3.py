# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time


# 配置文件地址
profile_directory = r"C:\Users\IBM_ADMIN\AppData\Roaming\Mozilla\Firefox\Profiles\3fyggsfu.default"
 
# 加载配置配置
profile = webdriver.FirefoxProfile(profile_directory)
# 启动浏览器配置
driver = webdriver.Firefox(profile)

#driver = webdriver.Firefox()
url = "https://www.baidu.com"
driver.get(url)
time.sleep(3)
mouse = driver.find_element("link text", u"设置")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(3)

#driver.find_element_by_link_text(u"搜索设置").click()
driver.find_element_by_css_selector('.setpref').click()
#driver.find_element("link text", u"搜索设置").click()
time.sleep(3)
s = driver.find_element("id", "nr")
Select(s).select_by_visible_text(u"每页显示50条")

# 方法一：先点父元素 交流QQ群：232607095
# driver.find_element("id", "gxszButton").click()
# driver.find_element("class name", "prefpanelgo").click()

# 方法二：用js直接去点击 交流QQ群：232607095
js = 'document.getElementsByClassName("prefpanelgo")[0].click();'
driver.execute_script(js)

time.sleep(2)
driver.switch_to_alert().accept()

time.sleep(2)
#driver.quit()
driver.close()

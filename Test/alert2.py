#coding=utf-8

from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
#from selenium.common.exceptions import UnexpectedAlertPresentException
#from selenium.common.exceptions import NoAlertPresentException

import time

# 配置文件地址
profile_directory = r"C:\Users\IBM_ADMIN\AppData\Roaming\Mozilla\Firefox\Profiles\3fyggsfu.default"
 
# 加载配置配置
profile = webdriver.FirefoxProfile(profile_directory)
# 启动浏览器配置
driver = webdriver.Firefox(profile)
#driver=webdriver.Firefox()

driver.implicitly_wait(10)

driver.get("https://www.baidu.com")

 

#mouse stop set link

link=driver.find_element_by_name("tj_settingicon")

ActionChains(driver).move_to_element(link).perform()

time.sleep(1)

#open search setting

#driver.find_element_by_link_text(u"搜索设置").click()
driver.find_element_by_css_selector('.setpref').click()
#driver.find_element_by_link_text(u"搜索历史").click()

#save set
#driver.find_element_by_css_selector('#gxszButton > a.prefpanelgo').click()
#driver.find_element_by_class_name('prefpanelgo').click()
driver.find_element_by_link_text(u"保存设置").click()
#driver.find_element_by_xpath("//input[@value='保存设置']").click()
#driver.find_element_by_css_selector('.prefpanelgo').click()
time.sleep(2)
#recieve pop_window

driver.switch_to_alert().accept()

time.sleep(2)
#driver.quit()
driver.close()

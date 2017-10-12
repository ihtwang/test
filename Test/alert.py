#coding=utf-8

from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Firefox()

driver.get("https://www.baidu.com")

driver.implicitly_wait(10)



link=driver.find_element_by_xpath("//*[@id='s_usersetting_top']/span")
#ActionChains(driver).move_to_element(set_link).perform()            #鼠标移动到设置上
#driver.find_element_by_xpath("//a[@class='setpref']").click()       #点击搜索设置链接
driver.execute_script('$(arguments[0]).click()',link)    
#time.sleep(3)    #加等待时间 等按钮可用，否则会报错

#link = driver.find_element_by_link_text('设置')
#link = driver.find_element_by_css_selector('.setting-text')
#link = driver.find_element_by_xpath("//*[@id='s_usersetting_top']/span")
#link = driver.find_element_by_class_name('setting-text')
#time.sleep(2)
#action = ActionChains(driver)
#action.move_to_element(link).perform()
#time.sleep(2)
#driver.find_element_by_class_name('setpref').click()
#driver.find_element_by_xpath("//*[@id='wrapper']/div[5]/a[1]").click()
#driver.find_element_by_link_text(u"登陆").click()
        #driver.find_element_by_xpath("//input[@value='保存设置']").click()

#time.sleep(2)


#link=driver.find_element_by_name("tj_settingicon")

#ActionChains(driver).move_to_element(link).perform()

#open search setting
#driver.find_element_by_link_text(u"设置").click()
#driver.find_element_by_xpath("//*[@id='wrapper']/div[5]/a[1]").click()
driver.find_element_by_link_text('搜索设置').find_element_by_link_text('搜索设置').click()

#save set

driver.find_element_by_link_text('保存设置').click()


#driver.find_element_by_css_selector('#gxszButton > a.frefpanelgo').click()
#driver.find_element_by_class_name('frefpanelgo').click()
time.sleep(2)

#driver.switch_to_alert().accept()

driver.quit()

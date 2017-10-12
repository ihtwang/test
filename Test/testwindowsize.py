#coding=utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.maximize_window()
print "*****"
print driver.get_window_size()
print "设置浏览器宽480、高800 显示"
driver.set_window_size(480, 800)
print driver.get_window_size()
driver.get("http://m.mail.10086.cn")
#参数数字为像素点

driver.quit()

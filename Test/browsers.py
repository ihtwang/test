#coding=utf-8
import time
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#浏览器数组
#lists=['chrome','firefox','internet explorer']
lists=['firefox','internet explorer']
#读取不同的浏览器执行脚本
'''
for browser in lists:
    print browser
    driver = Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities={'platform': 'ANY',
                        'browserName':browser,
                        'version': '',
                        'javascriptEnabled': True,
                        'marionette': False
                        })
'''

'''
driver = Remote(command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
            )
'''
'''
driver = Remote(command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX
            )
            '''

driver = Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities={'platform': 'ANY',
                        'browserName':'firefox',
                        'version': '',
                        'javascriptEnabled': True,
                        'marionette': False
                        })

driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys('browser')
driver.find_element_by_id("su").click()
time.sleep(10)
driver.close()

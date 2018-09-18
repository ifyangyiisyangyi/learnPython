# -*- coding: utf-8 -*-

import appium
from appium import webdriver
from time import sleep 

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0.0'
desired_caps['deviceName'] = '98895a365330393250'
desired_caps['app'] = 'C:/Users/yangy/Desktop/android apk/1.3.0/lookluka-release (1).apk'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

print("OK")
sleep(10)
driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="RootLayout"]/android.widget.RelativeLayout/android.widget.TextView').click()
sleep(2)
loginBtn = driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="RootLayout"]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button[1]')
loginBtn.click()
# 选中账号输入框
input = driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="RootLayout"]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.EditText')
input.send_keys("18101287746")
driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="RootLayout"]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.EditText').send_keys("yang598")
sleep(10)
driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="RootLayout"]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.Button').click()
#点击界面
sleep(5)
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout').click()
# 点击菜单栏
# driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageButton').click()
#点击我的宝宝
# sleep(2)
# print('its here')
# driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView').click()

# 点击绘本栏
sleep(2)
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/ai.ling.skel.view.FreeLayoutRadioGroup/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.RadioButton').click()

#向下滑动
sleep(2)
def get_size(driver):
	x = driver.get_window_size()['width']
	y = driver.get_window_size()['height']
	return (x,y)
def swipe_down(driver, t = 1000):
	i = get_size(driver)
	x1 = int(i[0] * 0.5)
	y1 = int(i[1] * 0.25)
	y2 = int(i[1] * 0.75)
	driver.swipe(x1, y1, x1, y2, t)
swipe_down(driver)

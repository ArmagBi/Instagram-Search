from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, urllib.request
import requests

driver = webdriver.Firefox()
driver.get("https://www.instagram.com/")

#login
time.sleep(5)
username = driver.find_element_by_css_selector("input[name='username']")
password = driver.find_element_by_css_selector("input[name='password']")
username.clear()
password.clear()
username.send_keys("armagbi")
password.send_keys("Shiy123456")
login = driver.find_element_by_css_selector("button[type='submit']").click()

#save your login info?
time.sleep(10)
notnow = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
#turn on notif
time.sleep(5)
notnow2 = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

#searchbox
time.sleep(2)
for i in range(0,200):
        X = 0
        X += i
        time.sleep(1)
        searchbox = driver.find_element_by_css_selector("input[placeholder='Search']")
        searchbox.clear()
        searchbox.send_keys("e")
        time.sleep(5)
        searchbox.send_keys(Keys.ENTER)
        searchbox.send_keys(X * (Keys.DOWN))
        time.sleep(0.5)
        searchbox.send_keys(Keys.ENTER)
        with open('F:\PycharmProjects\Test\Result.txt', 'a+') as f:
                print(driver.current_url.replace('https://www.instagram.com/'+'/', ''), file=f)
        





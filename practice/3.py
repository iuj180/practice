from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r'D:\blindcat\practice\chromedriver.exe')

driver.get('http://www.google.co.kr/')

time.sleep(3)

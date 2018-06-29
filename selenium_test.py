from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user = ""
pwd = ""
driver = webdriver.Chrome('./files/drivers/chromedriver.exe')
driver.get("http://www.facebook.com")
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()
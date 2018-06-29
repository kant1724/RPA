from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
user = ""
pwd = ""
#driver = webdriver.Chrome('./files/drivers/chromedriver.exe')
cap = DesiredCapabilities.INTERNETEXPLORER
cap['ignoreProtectedModeSettings'] = True
cap['IntroduceInstabilityByIgnoringProtectedModeSettings'] = True
cap['nativeEvents'] = True
cap['ignoreZoomSetting'] = True
cap['requireWindowFocus'] = True
cap['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True
driver = webdriver.Ie(capabilities=cap, executable_path='./files/drivers/IEDriverServer64.exe')
driver.get("http://www.facebook.com")
driver.maximize_window()
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()

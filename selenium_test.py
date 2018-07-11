from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from contextlib import contextmanager

@contextmanager
def wait_for_page_load(driver, timeout=30.0):
    source = driver.page_source
    yield
    WebDriverWait(driver, timeout, ignored_exceptions=(WebDriverException,)).until(lambda d: source != d.page_source)
#driver = webdriver.Chrome('./files/drivers/chromedriver.exe')
cap = DesiredCapabilities.INTERNETEXPLORER
cap['ignoreProtectedModeSettings'] = True
cap['IntroduceInstabilityByIgnoringProtectedModeSettings'] = True
cap['nativeEvents'] = True
cap['ignoreZoomSetting'] = True
cap['requireWindowFocus'] = True
cap['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True
driver = webdriver.Ie(capabilities=cap, executable_path='./files/drivers/IEDriverServer64.exe')
with wait_for_page_load(driver):
    driver.get('https://youtube.com/')
with wait_for_page_load(driver):
    driver.get('https://github.com/')

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def get_ie_driver():
    cap = DesiredCapabilities.INTERNETEXPLORER
    cap['ignoreProtectedModeSettings'] = True
    cap['IntroduceInstabilityByIgnoringProtectedModeSettings'] = True
    cap['nativeEvents'] = True
    cap['ignoreZoomSetting'] = True
    cap['requireWindowFocus'] = True
    cap['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True
    driver = webdriver.Ie(capabilities=cap, executable_path='./files/drivers/IEDriverServer64.exe')
    
    return driver
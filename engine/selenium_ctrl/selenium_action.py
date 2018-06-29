from engine.selenium_ctrl import selenium_get_driver
def ie_full_screen():
    ie_driver = selenium_get_driver.get_ie_driver()
    ie_driver.maximize_window()

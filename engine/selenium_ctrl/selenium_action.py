from engine.selenium_ctrl import selenium_get_driver

class Selenium_action():    
    ie_driver = None
    def ie_open(self):
        self.ie_driver = selenium_get_driver.get_ie_driver()
    
    def ie_full_screen(self):
        self.ie_driver.maximize_window()
    
    def ie_go_to_site(self, site_name):
        self.ie_driver.get(site_name)

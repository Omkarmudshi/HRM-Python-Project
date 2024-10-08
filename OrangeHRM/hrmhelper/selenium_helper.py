# all the method that are use for clicking,selecting and action chain

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Selenium_helper:
    def __init__(self,driver):
        self.driver=driver

    def webelement_enter(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)
    
    def webelement_click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

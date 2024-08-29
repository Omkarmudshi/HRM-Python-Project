#login page


from hrmhelper.selenium_helper import Selenium_helper
from selenium.webdriver.common.by import By
class Login_page(Selenium_helper):

    email_ele=(By.XPATH,"//input[@name='username']")
    password_ele=(By.XPATH,"//input[@name='password']")
    login_btn=(By.XPATH,"//button")

    def __init__(self, driver):
        super().__init__(driver)    #to something to the super contructor we use super method

    def login(self, username,password):
        self.webelement_enter(self.email_ele,username)
        self.webelement_enter(self.password_ele,password)
        self.webelement_click(self.login_btn)
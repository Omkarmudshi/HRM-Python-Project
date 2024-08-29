from conftest import *
import pytest
from hrmpages.Login_page import *


@pytest.mark.usefixtures("browser_setup")
class Test_login:

    def setup_class(self):
        self.driver.get(baseurl)
        self.login_page=Login_page(self.driver)

    def test_valid_login(self):
        self.login_page.login(Username,Password)

    def teardown_class(self):
        self.driver.quit()
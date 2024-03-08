import pytest
import allure
from tests.base_case import BaseCase
from src.pages import SampleAppPage


@allure.feature("Sample App")
class TestSampleApp(BaseCase):
    @allure.title("TC#1: Verify Sample App page is accessible")
    def test_sa_01_access_page(self):
        sa_page = SampleAppPage(self.driver)
        sa_page.open()
        assert sa_page.is_opened()

    @allure.title("TC#2: Verify successful login")
    @pytest.mark.parametrize("user,pwd,login_status", [("QATester", "pwd", "text-success")])
    def test_sa_02_successful_login(self, user, pwd, login_status):
        sa_page = SampleAppPage(self.driver)
        sa_page.open()
        # Fill in username and password (DEFAULT: pwd)
        sa_page.fill_username_field(user)
        sa_page.fill_pwd_field(pwd)
        # Click button to login
        sa_page.click_login_btn()
        # Verify login status is correct
        sa_page.check_login_status()
        assert sa_page.login_status.get_attribute("class") == login_status
        assert sa_page.login_status.text == "Welcome, " + user + "!"

    @allure.title("TC#3: Verify incorrect password")
    @pytest.mark.parametrize("user,pwd,login_status", [("QATester", "invalid123", "text-danger")])
    def test_sa_03_incorrect_password(self, user, pwd, login_status):
        sa_page = SampleAppPage(self.driver)
        sa_page.open()
        # Fill in username
        sa_page.fill_username_field(user)
        sa_page.fill_pwd_field(pwd)
        # Click button to login
        sa_page.click_login_btn()
        # Verify login status is correct
        sa_page.check_login_status()
        assert sa_page.login_status.get_attribute("class") == login_status
        assert sa_page.login_status.text == "Invalid username/password"

    @allure.title("TC#4: Verify if user logged out successfully")
    @pytest.mark.parametrize("user,pwd,login_status", [("QATester", "pwd", "text-success")])
    def test_sa_04_logout_user(self, user, pwd, login_status):
        sa_page = SampleAppPage(self.driver)
        sa_page.open()
        # Fill in username
        sa_page.fill_username_field(user)
        sa_page.fill_pwd_field(pwd)
        # Click button to login
        sa_page.click_login_btn()
        # Verify login status is correct
        sa_page.check_login_status()
        assert sa_page.login_status.get_attribute("class") == login_status
        assert sa_page.login_status.text == "Welcome, " + user + "!"
        # Logout user to check status
        sa_page.click_logout_btn()
        assert sa_page.login_status.text == "User logged out."


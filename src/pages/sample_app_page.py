import allure
from src.locators import SampleAppPageLocators
from src.base import BasePage
from src.links import Links


class SampleAppPage(BasePage):
    PAGE_URL = Links.SAMPLE_APP_PAGE
    LOCATORS = SampleAppPageLocators()

    @property
    def input_username(self):
        return self.find_element(self.LOCATORS.SAMPLE_APP_USERNAME)

    @property
    def input_password(self):
        return self.find_element(self.LOCATORS.SAMPLE_APP_PASSWORD)

    @property
    def button_login(self):
        return self.find_element(self.LOCATORS.SAMPLE_APP_LOGIN_BTN)

    @property
    def button_logout(self):
        return self.find_element(self.LOCATORS.SAMPLE_APP_LOGOUT_BTN)

    @property
    def login_status(self):
        return self.find_element(self.LOCATORS.SAMPLE_APP_LOGIN_STATUS)

    @allure.step("Fill input field for username")
    def fill_username_field(self, value: str):
        self.input_username.clear()
        self.input_username.send_keys(value)

    @allure.step("Fill input field for password")
    def fill_pwd_field(self, value: str):
        self.input_password.clear()
        self.input_password.send_keys(value)

    @allure.step("Click Login button")
    def click_login_btn(self):
        self.button_login.click()

    @allure.step("Click Logout button")
    def click_logout_btn(self):
        self.button_logout.click()

    @allure.step("Check Login Status")
    def check_login_status(self):
        self.login_status.is_displayed()


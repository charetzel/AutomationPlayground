import allure
from selenium.webdriver.support import expected_conditions as EC
from src.locators import LoadDelayLocators
from src.base import BasePage
from src.links import Links


class LoadDelayPage(BasePage):
    PAGE_URL = Links.LOAD_DELAY_PAGE
    LOCATORS = LoadDelayLocators

    @property
    def load_delay_link(self):
        return self.find_element(self.LOCATORS.LOAD_DELAY_LINK)

    @property
    def load_delay_button(self):
        return self.find_element(self.LOCATORS.LOAD_DELAY_BUTTON)

    @allure.step("Click Load Delay link")
    def click_load_delay_link(self):
        self.wait().until(self.load_delay_link.is_displayed())
        self.load_delay_link.click()

    @allure.step("Click Load Delay button")
    def click_load_delay_btn(self):
        self.load_delay_button.click()

    @allure.step("Wait for page load")
    def wait_for_page_load(self, element):
        # self.wait().until(self.load_delay_button.is_displayed())
        self.wait().until(EC.visibility_of_element_located(element))

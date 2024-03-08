import allure

from selenium.webdriver.common.action_chains import ActionChains
from src.locators import ClickLocators
from src.base import BasePage
from src.links import Links


class ClickPage(BasePage):
    PAGE_URL = Links.CLICK_PAGE
    LOCATORS = ClickLocators()

    @property
    def bad_btn(self):
        return self.find_element(self.LOCATORS.CLICK_BAD_BTN)

    @property
    def success_btn(self):
        return self.find_element(self.LOCATORS.CLICK_SUCCESS_BTN)

    @allure.step("Click bad button")
    def click_bad_btn(self):
        AC = ActionChains(self.driver)
        AC.click(self.bad_btn).perform()

    @allure.step("Verify if success btn is displayed, then click")
    def click_success_btn(self):
        self.success_btn.click()

import allure
from src.locators import TextInputLocators
from src.base import BasePage
from src.links import Links


class TextInputPage(BasePage):
    PAGE_URL = Links.TEXT_INPUT_PAGE
    LOCATORS = TextInputLocators()

    @property
    def input_field(self):
        return self.find_element(self.LOCATORS.TEXT_INPUT_FIELD)

    @property
    def update_button(self):
        return self.find_element(self.LOCATORS.TEXT_INPUT_BTN)

    @allure.step("Input text in text field")
    def fill_text_field(self, value: str):
        self.input_field.send_keys(value)

    @allure.step("Click button to update")
    def click_update_btn(self):
        self.update_button.click()


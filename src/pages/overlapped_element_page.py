import allure

from src.locators import OverlappedElementLocators
from src.base import BasePage
from src.links import Links


class OverlappedElementPage(BasePage):
    PAGE_URL = Links.OVERLAPPED_ELEMENT_PAGE
    LOCATORS = OverlappedElementLocators()

    @property
    def field_id(self):
        return self.find_element(self.LOCATORS.OVERLAPPED_ELEMENT_ID)

    @property
    def field_name(self):
        return self.find_element(self.LOCATORS.OVERLAPPED_ELEMENT_NAME)

    @property
    def overlapped_element(self):
        return self.find_element(self.LOCATORS.OVERLAPPED_ELEMENT_SUBJECT)

    @allure.step("Fill input field for Id")
    def fill_id_field(self, value: str):
        self.field_id.send_keys(value)

    @allure.step("Fill input field for Name")
    def fill_name_field(self, value: str):
        self.field_name.send_keys(value)

    @allure.step("Scroll to desired element")
    def scroll_page(self):
        self.field_name.location_once_scrolled_into_view.get(self.fill_name_field)


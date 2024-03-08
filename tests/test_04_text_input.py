import pytest
import allure
from tests.base_case import BaseCase
from src.pages import TextInputPage


@allure.feature("Text Input")
class TestTextInput(BaseCase):
    @allure.title("TC#1: Verify Text Input page is accessible")
    def test_txt_01_access_page(self):
        txt_page = TextInputPage(self.driver)
        txt_page.open()
        assert txt_page.is_opened()

    @allure.title("TC#2: Verify that button text is updated")
    @pytest.mark.parametrize("text", ["Test update button name"])
    def test_tx_01_update_btn_name(self, text):
        txt_page = TextInputPage(self.driver)
        txt_page.open()
        assert txt_page.is_opened()
        txt_page.fill_text_field(text)
        txt_page.click_update_btn()
        assert txt_page.update_button.text == text

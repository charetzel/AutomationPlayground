import pytest
import allure
from tests.base_case import BaseCase
from src.pages import ClickPage


@allure.feature("Click")
class TestClick(BaseCase):
    @allure.title("TC#1: Verify that button is clicked")
    def test_click_01_verify_btn_is_clicked(self):
        click_page = ClickPage(self.driver)
        click_page.open()
        assert click_page.is_opened()
        # Click button in page (Using ActionChains)
        click_page.click_bad_btn()
        # Checks if button was clicked
        assert click_page.success_btn.is_displayed()

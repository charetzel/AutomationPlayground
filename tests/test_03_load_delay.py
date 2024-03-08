import pytest
import allure
from tests.base_case import BaseCase
from src.pages import LoadDelayPage


@allure.feature("Load Delay")
class TestLoadDelay(BaseCase):
    @allure.title("TC#1: Verify Load Delay link page is loaded")
    def test_ld_01_check_page_load(self):
        ld_page = LoadDelayPage(self.driver)
        # Navigate to Homepage
        ld_page.open()
        assert ld_page.is_opened()
        ld_page.driver.implicitly_wait(30)
        # Wait for load delay page load until button is displayed
        ld_page.wait().until(ld_page.load_delay_button.is_displayed())
        assert ld_page.load_delay_button.is_displayed()
        ld_page.click_load_delay_btn()
        ld_page.make_screenshot("load_delay_page_load")
        


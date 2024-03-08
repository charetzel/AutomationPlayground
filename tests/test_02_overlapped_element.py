import pytest
import allure
from tests.base_case import BaseCase
from src.pages import OverlappedElementPage


@allure.feature("Overlapped Element")
class TestOverlappedElementPage(BaseCase):

    @allure.title("TC#1: Verify page is accessible")
    def test_oe_01_access_page(self):
        oe_page = OverlappedElementPage(self.driver)
        oe_page.open()
        assert oe_page.is_opened()

    @allure.title("TC#2: Verify name field is editable")
    @pytest.mark.parametrize("name", ["AutomatedText"])
    def test_oe_02_fill_name_field(self, name):
        # Navigate to test page
        oe_page = OverlappedElementPage(self.driver)
        oe_page.open()
        # Scroll to name field element
        # Verify name field is displayed & editable
        oe_page.scroll_page()
        assert oe_page.field_name.is_displayed()
        oe_page.fill_name_field(name)
        oe_page.make_screenshot("edit_name_field")


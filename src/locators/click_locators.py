from selenium.webdriver.common.by import By
from src.base.base_locators import BasePageLocators


class ClickLocators(BasePageLocators):
    CLICK_BAD_BTN = (By.XPATH, "//*[@id='badButton']")
    CLICK_SUCCESS_BTN = (By.XPATH, "//*[@class='btn btn-success']")

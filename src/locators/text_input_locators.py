from selenium.webdriver.common.by import By
from src.base.base_locators import BasePageLocators


class TextInputLocators(BasePageLocators):
    TEXT_INPUT_FIELD = (By.XPATH, "//*[@id='newButtonName']")
    TEXT_INPUT_BTN = (By.XPATH, "//*[@id='updatingButton']")

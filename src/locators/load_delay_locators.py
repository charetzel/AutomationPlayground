from selenium.webdriver.common.by import By
from src.base.base_locators import BasePageLocators


class LoadDelayLocators(BasePageLocators):
    LOAD_DELAY_LINK = "//*[@href='/loaddelay']"
    LOAD_DELAY_BUTTON = "//*[@class='btn btn-primary']"

from selenium.webdriver.common.by import By
from src.base.base_locators import BasePageLocators


class OverlappedElementLocators(BasePageLocators):
    OVERLAPPED_ELEMENT_ID = (By.XPATH, "//*[@id='id']")
    OVERLAPPED_ELEMENT_NAME = (By.XPATH, "//*[@id='name']")
    OVERLAPPED_ELEMENT_SUBJECT = (By.XPATH, "//*[@id='subject']")

from selenium.webdriver.common.by import By
from src.base.base_locators import BasePageLocators


class SampleAppPageLocators(BasePageLocators):
    SAMPLE_APP_USERNAME = (By.XPATH, "//*[@name='UserName']")
    SAMPLE_APP_PASSWORD = (By.XPATH, "//*[@type='password']")
    SAMPLE_APP_LOGIN_BTN = (By.XPATH, "//button[@class='btn btn-primary']")
    SAMPLE_APP_LOGIN_STATUS = (By.XPATH, "//*[@id='loginstatus']")
    SAMPLE_APP_LOGOUT_BTN = (By.XPATH, "//button[text()='Log Out']")

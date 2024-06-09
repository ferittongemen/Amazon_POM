from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.login_locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.send_keys(By.ID, LoginPageLocators.EMAIL_FIELD, username)
        self.click(By.ID, LoginPageLocators.CONTINUE_BUTTON)
        self.send_keys(By.ID, LoginPageLocators.PASSWORD_FIELD, password)
        self.click(By.ID, LoginPageLocators.SIGN_IN_SUBMIT)
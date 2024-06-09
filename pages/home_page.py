import time

from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.home_locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate(self):
        self.driver.get("http://www.amazon.com")
        #Captcha'ya takılmamak privacy policy butonuna tıkla
        self.click(By.XPATH, HomePageLocators.PRIVACY_POLICY_BUTTON)

    def assert_home_page(self, title):
        assert title in self.driver.title

    def click_sign_in(self):
        self.click(By.ID, HomePageLocators.SIGN_IN_BUTTON)

    def search_item(self, item):
        self.send_keys(By.ID, HomePageLocators.SEARCH_BOX, item)
        self.click(By.ID, HomePageLocators.SEARCH_BUTTON)
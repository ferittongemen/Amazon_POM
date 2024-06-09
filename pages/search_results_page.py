import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from locators.search_results_locators import SearchResultsLocators

class SearchResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def assert_results_found(self, search_text):
        results_text = self.find_element(By.CSS_SELECTOR, SearchResultsLocators.RESULTS_TEXT)
        assert search_text.lower() in results_text.text.lower()

    def go_to_second_page(self):
        second_page_link = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((By.XPATH, SearchResultsLocators.SECOND_PAGE_LINK))
        )
        second_page_link.click()

        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.XPATH, SearchResultsLocators.SECOND_PAGE_LOADED_INDICATOR))
        )

    def assert_second_page(self, page_text):
        assert page_text in self.driver.current_url

    def go_to_third_product(self):
        third_product_link = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((By.XPATH, SearchResultsLocators.THIRD_PRODUCT_LINK))
        )
        third_product_link.click()

    def add_third_item_to_list(self):
        list_button_dropdown = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((By.ID, SearchResultsLocators.LISTEYE_EKLE_BUTTON_DROPDOWN))
        )
        list_button_dropdown.click()

        time.sleep(5)
        actions = ActionChains(self.driver)
        for _ in range(3):
            time.sleep(0.5)
            actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ENTER)
        actions.perform()
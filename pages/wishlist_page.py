from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.wishlist_locators import WishlistPageLocators

class WishlistPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def assert_item_in_wishlist(self, item_text):
        wishlist_items = self.find_elements(By.CSS_SELECTOR, WishlistPageLocators.WISHLIST_ITEMS)
        for item in wishlist_items:
            if item_text.lower() in item.text.lower():
                return True
        assert False, f"Item with text '{item_text}' not found in wishlist."

    def delete_item_from_wishlist(self):
        delete_button = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((By.NAME, WishlistPageLocators.DELETE_BUTTON))
        )
        delete_button.click()

    def assert_item_deleted(self, item_text):
        # Belirtilen XPATH içinde item_text olup olmadığını kontrol et
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.XPATH, WishlistPageLocators.DELETED_PRODUCT))
        )
        assert item_text.lower() in element.text.lower(), (f"Item with text '{item_text}' not found in the specified "
                                                           f"XPATH.")
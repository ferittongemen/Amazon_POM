import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_results_page import SearchResultsPage
from pages.wishlist_page import WishlistPage
from tests.test_data.test_data import TestData


class AmazonTest(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        self.driver.implicitly_wait(10)
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.wishlist_page = WishlistPage(self.driver)

    def test_amazon_workflow(self):
        self.home_page.navigate()
        self.home_page.assert_home_page(TestData.HOME_PAGE_TITLE)
        self.home_page.click_sign_in()
        self.login_page.login(TestData.USERNAME, TestData.PASSWORD)
        self.home_page.search_item(TestData.SEARCH_ITEM)
        self.search_results_page.assert_results_found(TestData.SEARCH_ITEM)
        self.search_results_page.go_to_second_page()
        self.search_results_page.assert_second_page(TestData.SECOND_PAGE_TEXT)
        self.search_results_page.go_to_third_product()
        self.search_results_page.add_third_item_to_list()
        self.wishlist_page.assert_item_in_wishlist(TestData.SEARCH_ITEM)
        self.wishlist_page.delete_item_from_wishlist()
        self.wishlist_page.assert_item_deleted(TestData.SEARCH_ITEM)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
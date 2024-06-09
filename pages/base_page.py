from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((by, value)))

    def find_elements(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located((by, value)))

    def click(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def send_keys(self, by, value, keys):
        element = self.find_element(by, value)
        element.send_keys(keys)

    def wait_for_element(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((by, value)))

    def wait_for_element_to_be_invisible(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element_located((by, value)))

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)
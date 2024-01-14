from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def transition_site(self, url):
        return self.driver.get(url)

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator))

    def find_element_located_click(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator)).click()

    def find_element_located_input(self, locator, text, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator)).send_keys(text)

    def find_elements_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator))

    def accept_the_cookies(self):
        return self.find_element_located_click(BasePageLocators.ACCEPT_COOKIES)

    def current_url(self):
        return self.driver.current_url

    def switch_window(self, num):
        self.driver.switch_to.window(self.driver.window_handles[num])

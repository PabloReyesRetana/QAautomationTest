import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from helpers.selectors import Selectors


class Actions:

    def __init__(self, driver):
        self.driver = driver
        self.wait_for_element_time = 15

    def wait_for_element(self, locator, locator_string):
        try:
            wait = WebDriverWait(self.driver, self.wait_for_element_time)
            wait.until(ec.presence_of_element_located((locator, locator_string)))
            wait.until(ec.visibility_of_element_located((locator, locator_string)))
            element = self.driver.find_element(locator, locator_string)
            return element
        except TimeoutException:
            self.fail_test("Element took too long to appear on screen")

    def log_in(self, user, password):
        try:
            self.wait_for_element(By.ID, Selectors.username_input).send_keys(user)
            self.wait_for_element(By.ID, Selectors.password_input).send_keys(password)
            self.wait_for_element(By.ID, Selectors.login_button).click()
            time.sleep(5)
        except:
            self.fail_test("Login element couldn't be located")

    def fail_test(self, failure_text):
        assert False, failure_text

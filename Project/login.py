import unittest
import HtmlTestRunner
from helpers.actions import Actions
from helpers.secrets import SecretKeys
from helpers.selectors import Selectors
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCases(unittest.TestCase, Actions):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.wait_for_element_time = 15

    def test_01_valid_login(self):
        try:
            self.driver.get(SecretKeys.web_url)
            self.log_in(SecretKeys.user, SecretKeys.password)
            self.wait_for_element(By.ID, Selectors.main_divider)
            menu = self.wait_for_element(By.ID, Selectors.user_menu)
            self.assertIn(SecretKeys.user, menu.text, "User is correctly logged in")
            menu.click()
            self.wait_for_element(By.CSS_SELECTOR, Selectors.log_out_button).click()
            self.wait_for_element(By.ID, Selectors.username_input)
        except:
            self.fail_test("Login test 01 failed")

    def test_02_invalid_login(self):
        try:
            self.driver.get(SecretKeys.web_url)
            self.log_in(SecretKeys.user, "wrong_password")
            self.wait_for_element(By.ID, Selectors.main_divider)
            self.fail_test("Login was successful regardless of wrong password")
        except:
            pass

    def test_03_empty_login(self):
        try:
            self.driver.get(SecretKeys.web_url)
            self.log_in('', '')
            pop_up = self.wait_for_element(By.ID, Selectors.login_text).text
            self.assertEqual(pop_up, "Please enter your username and password:")
        except:
            self.fail_test("Login pop up wasn't found")

    def test_04_forgot_password_access(self):
        try:
            self.driver.get(SecretKeys.web_url)
            self.wait_for_element(By.ID, Selectors.forgot_password).click()
            title = self.wait_for_element(By.CLASS_NAME, Selectors.center_text).text
            self.assertEqual(title, "Forgot Password")
        except:
            self.fail_test("'Forgot Password' page wasn't located")

    def test_05_privacy_policy_link(self):
        try:
            self.driver.get(SecretKeys.web_url)
            self.wait_for_element(By.CSS_SELECTOR, Selectors.privacy_policy_button).click()
            handles = self.driver.window_handles
            self.assertIs(len(handles), 2)
        except:
            self.fail_test("Privacy Policy link didn't worked correctly")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Finished")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports'))

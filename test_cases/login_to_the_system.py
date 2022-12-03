import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.Credentials import Credentials


class TestLoginPage(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.login_page = LoginPage(self.driver)
        self.base_page = BasePage(self.driver)
        self.credentials = Credentials(self.driver)
        self.dashboard_page = Dashboard(self.driver)

    """Successful logging in to the system"""
    def test_login_to_system(self):
        self.login_page.title_of_the_page()  # check that we are on proper page
        self.login_page.login(self.credentials.email, self.credentials.password)
        self.dashboard_page.title_of_the_page()  # check that after login in Dashboard opens

    def test_fail_login_to_system(self):
        self.login_page.title_of_the_page()  # check that we are on propper page
        self.login_page.login(email="a@gmail.com", password="12345")
        self.login_page.assert_element_text(self.driver, self.login_page.invalid_pass_error_xpath, expected_text='Identifier or password invalid.')

    def test_remind_password(self):
        self.login_page.remind_password()
        self.login_page.type_in_remind_pass(self.credentials.email)
        self.login_page.click_button_send_remind_pass()
        self.login_page.wait_for_popup()
        self.base_page.assert_element_text(self.driver, self.login_page.remind_pass_confirmation_popup_xpath, expected_text='Message sent successfully.')
        self.login_page.click_back_to_sign_in()


    """Check page header by text"""
    def test_check_by_text(self):
        self.base_page.assert_element_text(self.driver, self.login_page.header_text_xpath, expected_text='Scouts Panel')

    def test_change_language_english(self):
        self.login_page.change_language('EN')
        self.base_page.assert_element_text(self.driver, self.login_page.sign_in_button_xpath, expected_text="SIGN IN")

    def test_change_language_polish(self):
        self.login_page.change_language('PL')
        self.base_page.assert_element_text(self.driver, self.login_page.sign_in_button_xpath, expected_text='ZALOGUJ')

    @classmethod
    def tearDown(self):
        self.driver.quit()

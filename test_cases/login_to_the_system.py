import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
from pages.base_page import BasePage


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

    """Successful logging in to the system"""
    def test_login_to_system(self):
        self.login_page.title_of_the_page()  # check that we are on propper page
        self.login_page.type_in_email('user01@getnada.com')
        self.login_page.type_in_password('Test-1234')
        self.login_page.click_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_the_page()  # check that after login in Dashboard opens

    """Check page header by text"""
    def test_check_by_text(self):
        self.login_page.assert_element_text(self.driver, self.login_page.header_text_xpath, expected_text='Scouts Panel')

    def test_change_language_english(self):
        self.login_page.change_language('EN')
        time.sleep(3)
        self.login_page.assert_element_text(self.driver, self.login_page.sign_in_button_xpath, expected_text="Sign in")

    def test_change_language_polish(self):
        self.login_page.change_language('PL')
        time.sleep(3)
        self.login_page.assert_element_text(self.driver, self.login_page.sign_in_button_xpath, expected_text='Zaloguj')

    @classmethod
    def tearDown(self):
        self.driver.quit()

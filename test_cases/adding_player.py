import os
import unittest
from selenium import webdriver

from pages.add_a_player import AddPlayer
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
import time


class TestAddPlayer(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.login_page = LoginPage(self.driver)
        self.add_player = AddPlayer(self.driver)

    """Filling in form for new player"""
    def test_add_player(self):
        self.login_page.type_in_email("user01@getnada.com")
        self.login_page.type_in_password("Test-1234")
        self.login_page.click_button()
        time.sleep(5)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_button_add_player()
        time.sleep(3)
        self.add_player.type_in_email("anna_QA123@gmail.com")
        self.add_player.input_name("Harry")
        self.add_player.input_surname("Potter")
        self.add_player.input_age("10.09.1993")
        self.add_player.input_leg("12")
        self.add_player.input_club("Griffindor")
        self.add_player.input_height("179")
        self.add_player.input_weight("123")
        self.add_player.input_phone("0991071113")
        self.add_player.input_level("9")
        self.add_player.click_button()
        time.sleep(2)
        self.add_player.select_option()
        self.add_player.input_main_position("Wizard")
        self.add_player.click_button_submit()
        time.sleep(6)

    """Check header is correct"""
    def test_title_add_player(self):
        self.login_page.type_in_email("user01@getnada.com")
        self.login_page.type_in_password("Test-1234")
        self.login_page.click_button()
        time.sleep(2)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_button_add_player()
        time.sleep(2)
        actual_title = self.get_page_title('https://scouts-test.futbolkolektyw.pl/en/players/add')
        expected_title = 'Add player'
        assert actual_title == expected_title

    def get_page_title(self, url):
        return self.driver.title

    @classmethod
    def tearDown(self):
        self.driver.quit()


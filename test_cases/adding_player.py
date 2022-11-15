import os
import unittest
from selenium import webdriver

from pages.add_a_player import AddPlayer
from pages.base_page import BasePage
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

    @classmethod
    def tearDown(self):
        self.driver.quit()


    def test_add_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_button()
        time.sleep(5)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_button_add_player()
        time.sleep(3)
        add_player = AddPlayer(self.driver)
        add_player.type_in_email("anna_QA123@gmail.com")
        add_player.input_name("Harry")
        add_player.input_surname("Potter")
        add_player.input_age("10.09.1993")
        add_player.input_leg("12")
        add_player.input_club("Griffindor")
        add_player.input_height("179")
        add_player.input_weight("123")
        add_player.input_phone("0991071113")
        add_player.input_level("9")
        add_player.click_button()
        time.sleep(2)
        add_player.select_option()
        add_player.input_main_position("Wizard")
        add_player.click_button_submit()
        time.sleep(6)


    def test_title_add_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_button()
        time.sleep(5)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_button_add_player()
        time.sleep(2)
        actual_title = self.get_page_title('https://scouts-test.futbolkolektyw.pl/en/players/add')
        expected_title = 'Add player'
        assert actual_title == expected_title

    def get_page_title(self, url):
        return self.driver.title


from pages.base_page import BasePage
import time
from selenium.webdriver.common.by import By



class AddPlayer(BasePage):
    email_input_xpath = '//*[@name="email"]'
    name_input_xpath = '//*[@name="name"]'
    surname_input_xpath = '//*[@name="surname"]'
    phone_input_xpath = '//*[@name="phone"]'
    weight_select_xpath = '//*[@name="weight"]'
    height_select_xpath = '//*[@name="height"]'
    age_select_xpath = '//*[@name="age"]'
    leg_select_xpath = '//*[@id="mui-component-select-leg"]'
    left_leg_xpath = '//*[@data-value="left"]'
    right_leg_xpath = '//*[@data-value="right"]'
    club_input_xpath = '//*[@name="club"]'
    level_input_xpath = '//*[@name="level"]'
    main_position_input_xpath = '//*[@name="mainPosition"]'
    second_position_input_xpath = '//*[@name="secondPosition"]'
    district_list_xpath = '//*[@id="menu-district"]/div[3]/ul/li'
    district_xpath = '//*[@id="mui-component-select-district"]'
    achievements_input_xpath = '//*[@name="achievements"]'
    submit_button_xpath = '//*[@type="submit"]'
    add_language_button_xpath = '//*[text()="Dodaj język" or text()="Add language"]'
    language_input_xpath = '//input[contains(@name, "languages")]'
    player_add_success_popup = '//*[text()="Added player." or text()="Dodano gracza."]'

    def type_in_email(self, email):
        self.field_send_keys(self.email_input_xpath, email)

    def input_name(self, name):
        self.field_send_keys(self.name_input_xpath, name)

    def input_surname(self, surname):
        self.field_send_keys(self.surname_input_xpath, surname)

    def input_phone(self, phone):
        self.field_send_keys(self.phone_input_xpath, phone)

    def input_weight(self,  weight):
        self.field_send_keys(self.weight_select_xpath,  weight)

    def input_height(self,  height):
        self.field_send_keys(self.height_select_xpath, height)

    def input_age(self,  age):
        self.field_send_keys(self.age_select_xpath, age)


    def input_club(self,  club):
        self.field_send_keys(self.club_input_xpath,  club)

    def input_level(self,  level):
        self.field_send_keys(self.level_input_xpath,  level)

    def click_button_submit(self):
        self.click_on_the_element(self.submit_button_xpath)

    def input_main_position(self,  main_position):
        self.field_send_keys(self.main_position_input_xpath,  main_position)

    def input_second_position(self, second_position):
        self.field_send_keys(self.second_position_input_xpath, second_position)

    def select_leg(self, leg):
        self.click_on_the_element(self.leg_select_xpath)
        if leg == "Left":
            self.click_on_the_element(self.left_leg_xpath)
        else:
            self.click_on_the_element(self.right_leg_xpath)

    def input_achievements(self, achievements):
        self.field_send_keys(self.achievements_input_xpath, achievements)

    def add_language(self, language):
        self.click_on_the_element(self.add_language_button_xpath)
        self.wait_for_element_to_be_clickable(self.language_input_xpath)
        time.sleep(4)
        self.field_send_keys(self.language_input_xpath, language)


    def select_district(self, value):
        self.click_on_the_element(self.district_xpath)
        time.sleep(2)
        self.click_on_the_element(selector='//*[@id="menu-district"]/div[3]/ul/li'+'['+value+']')












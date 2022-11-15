from pages.base_page import BasePage
import time


class AddPlayer(BasePage):
    email_input_xpath = '//*[@name="email"]'
    name_input_xpath = '//*[@name="name"]'
    surname_input_xpath = '//*[@name="surname"]'
    phone_input_xpath = '//*[@name="phone"]'
    weight_select_xpath = '//*[@name="weight"]'
    height_select_xpath = '//*[@name="height"]'
    age_select_xpath = '//*[@name="age"]'
    leg_select_xpath = '//*[@name="leg"]'
    club_input_xpath = '//*[@name="club"]'
    level_input_xpath = '//*[@name="level"]'
    main_position_input_xpath = '//*[@name="mainPosition"]'
    second_position_input_xpath = '//*[@name="secondPosition"]'
    district_select_xpath = '//*[@id="menu-district"]/div[3]//li[5]'
    district_xpath = '//*[@id="mui-component-select-district"]'
    achievements_input_xpath = '//*[@name="achievements"]'
    submit_button_xpath = '//*[@type="submit"]'

    def type_in_email(self, email):
        self.field_send_keys(self.email_input_xpath, email)

    def input_name(self, name):
        self.field_send_keys(self.name_input_xpath, name)

    def input_surname(self, surname):
        self.field_send_keys(self.surname_input_xpath, surname)

    def input_phone(self, phone):
        self.field_send_keys(self.phone_input_xpath, phone)

    def click_button(self):
        self.click_on_the_element(self.district_xpath)
        time.sleep(5)

    def select_option(self):
        self.click_on_the_element(self.district_select_xpath)
        time.sleep(5)

    def input_weight(self,  weight):
        self.field_send_keys(self.weight_select_xpath,  weight)

    def input_height(self,  height):
        self.field_send_keys(self.height_select_xpath, height)

    def input_age(self,  age):
        self.field_send_keys(self.age_select_xpath, age)

    def input_leg(self,  leg):
        self.field_send_keys(self.leg_select_xpath,  leg)

    def input_club(self,  club):
        self.field_send_keys(self.club_input_xpath,  club)

    def input_level(self,  level):
        self.field_send_keys(self.level_input_xpath,  level)

    def click_button_submit(self):
        self.click_on_the_element(self.submit_button_xpath)

    def input_main_position(self,  main_position):
        self.field_send_keys(self.main_position_input_xpath,  main_position)








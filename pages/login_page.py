from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):
     login_url = 'https://scouts-test.futbolkolektyw.pl/login'
     expected_title = 'Scouts panel - sign in'
     login_field_xpath = '//*[@id="login"]'
     password_field_xpath = '//*[@id="password"]'
     sign_in_button_xpath = '//*[text()="Sign in" or text()="Zaloguj"]'
     header_text_xpath = '//*[text()="Scouts Panel"]'
     login_label_xpath = '//*[@id="login-label"]'
     password_label_xpath = '//*[@id="password-label"]'
     language_select_xpath = '//div[contains(@aria-haspopup, "listbox")]'
     select_english_xpath = '//*[@id="menu-"]//li[2]'
     select_polish_xpath = '//*[@id="menu-"]//li[1]'


     def type_in_email(self, email):
         self.field_send_keys(self.login_field_xpath, email)

     def type_in_password(self, password):
         self.field_send_keys(self.password_field_xpath, password)

     def click_button(self):
          self.click_on_the_element(self.sign_in_button_xpath)

     def change_language(self, language):
          self.click_on_the_element(self.language_select_xpath)
          if language == 'EN':
               self.click_on_the_element(self.select_english_xpath)
          else:
               self.click_on_the_element(self.select_polish_xpath)


     def title_of_the_page(self):
          self.wait_for_element_to_be_clickable(self.expected_title)
          assert self.get_page_title(self.login_url) == self.expected_title

     def assert_element_text(self, driver, xpath, expected_text):
          """Comparing expected text with observed value from web element

              :param driver: webdriver instance
              :param xpath: xpath to element with text to be observed
              :param expected_text: text what we expecting to be found
              :return: None
          """
          element = driver.find_element(by=By.XPATH, value=xpath)
          element_text = element.text
          assert expected_text == element_text

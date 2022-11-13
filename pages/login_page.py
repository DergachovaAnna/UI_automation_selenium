from pages.base_page import BasePage
import time


class LoginPage(BasePage):
     login_url = "https://scouts-test.futbolkolektyw.pl/login"
     expected_title = "Scouts panel - sign in"
     login_field_xpath = "//*[@id='login']"
     password_field_xpath = "//*[@id='password']"
     sign_in_button_xpath = "//*[text()='Sign in' or text()='Zaloguj']"
     header_text_xpath = "//*[text()='Scouts Panel']"
     login_label_xpath = "//*[@id='login-label']"
     password_label_xpath = "//*[@id='password-label']"
     language_select_xpath = "//div[contains(@aria-haspopup, 'listbox')]"

     def type_in_email(self, email):
         self.field_send_keys(self.login_field_xpath, email)

     def type_in_password(self, password):
         self.field_send_keys(self.password_field_xpath, password)

     def click_button(self):
          self.click_on_the_element(self.sign_in_button_xpath)

     def title_of_the_page(self):
          time.sleep(5)
          assert self.get_page_title(self.login_url) == self.expected_title



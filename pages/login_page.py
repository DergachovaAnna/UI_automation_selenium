from pages.base_page import BasePage





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
     invalid_pass_error_xpath = "//form//div[1]/div[3]/span"
     remind_password_xpath = "//form//a"
     remind_pass_input_xpath = "//input[@name='email']"
     send_button_remind_pass_xpath = "//*/button"
     remind_pass_confirmation_popup_xpath = "//*[@role='alert']"
     back_to_sign_in_xpath = "//*/a"



     def type_in_email(self, email):
         self.field_send_keys(self.login_field_xpath, email)

     def type_in_password(self, password):
         self.field_send_keys(self.password_field_xpath, password)

     def click_button(self):
          self.click_on_the_element(self.sign_in_button_xpath)

     def login(self, email, password):
          self.type_in_email(email)
          self.type_in_password(password)
          self.click_button()

     def type_in_remind_pass(self, email):
          self.field_send_keys(self.remind_pass_input_xpath, email)

     def remind_password(self):
          self.click_on_the_element(self.remind_password_xpath)

     def click_button_send_remind_pass(self):
         self.click_on_the_element(self.send_button_remind_pass_xpath)


     def change_language(self, language):
          self.click_on_the_element(self.language_select_xpath)
          if language == 'EN':
               self.click_on_the_element(self.select_english_xpath)
          else:
               self.click_on_the_element(self.select_polish_xpath)


     def title_of_the_page(self):
          assert self.get_page_title(self.login_url) == self.expected_title


     def wait_for_popup(self):
          self.wait_for_element_to_be_clickable(self.remind_pass_confirmation_popup_xpath)


     def click_back_to_sign_in(self):
          self.click_on_the_element(self.back_to_sign_in_xpath)






from pages.base_page import BasePage


class LoginPage(BasePage):
     login_field_xpath = "//*[@id='login']"
     password_field_xpath = "//*[@id='password']"
     sign_in_button_xpath = "//button/span[2]"
     header_text_xpath = "//*[text()='Scouts Panel']"
     login_label_xpath = "//*[@id='login-label']"
     password_label_xpath = "//*[@id='password-label']"
     language_select_xpath = "//div[contains(@aria-haspopup, 'listbox')]"


     def type_in_email(self, email):
         self.field_send_keys(self.login_field_xpath, email)

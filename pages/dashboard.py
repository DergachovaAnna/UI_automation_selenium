from pages.base_page import BasePage
import time


class Dashboard(BasePage):
    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    main_page_button_xpath = '//*[text()="Main page" or  text()="Strona główna"]//ancestor::*[@role="button"]'
    players_button_xpath = '//*[text()="Players" or text()="Gracze"]//ancestor::*[@role="button"]'
    language_button_xpath = '//*[text()="English" or text()="Polski"]//ancestor::*[@role="button"]'
    sign_out_button_xpath = '//*[text()="Sign out" or text()="Wyloguj"]//ancestor::*[@role="button"]'
    block_players_xpath = '//main//div[1][contains(@class, "MuiGrid-grid-xs-6")]'
    block_matches_xpath = '//main//div[2][contains(@class, "MuiGrid-grid-xs-6")]'
    block_reports_xpath = '//main//div[3][contains(@class, "MuiGrid-grid-xs-6")]'
    block_events_xpath = '//main//div[4][contains(@class, "MuiGrid-grid-xs-6")]'
    add_player_button_xpath = '//a[contains(@href, "/players/add")]/button'
    dev_contact_link_xpath = '//a[contains(@href, "https://app.slack.com/")]'
    logo_xpath = '//*[@title="Logo Scouts Panel"]'
    main_header_xpath = '//h2[text()="Scouts Panel"]'
    main_panel_text_xpath = '//main//p'
    last_cr_player_button_xpath = '//a[1][contains(@href, "edit")]/button'
    last_upd_player_button_xpath = '//a[2][contains(@href, "edit")]/button'
    last_cr_match_button_xpath = '//a[3][contains(@href, "match")]/button'
    last_upd_match_button_xpath = '//a[4][contains(@href, "match")]/button'
    last_upd_report_button_xpath = '//a[5][contains(@href, "reports")]/button'

    def title_of_the_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_button(self):
        self.click_on_the_element(self.add_player_button_xpath)



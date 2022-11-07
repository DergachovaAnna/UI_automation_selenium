from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_button_xpath = "//span[text()='Main page' or  text()='Strona główna']//ancestor::div[@role='button']"
    players_button_xpath = "//span[text()='Players' or text()='Gracze']//ancestor::div[@role='button']"
    language_button_xpath = "//span[text()='English' or text()='Polski']//ancestor::div[@role='button']"
    sign_out_button_xpath = "//span[text()='Sign out' or text()='Wyloguj']//ancestor::div[@role='button']"
    block_players_xpath = "//main//div[1][contains(@class, 'MuiGrid-grid-xs-6')]"
    block_matches_xpath = "//main//div[2][contains(@class, 'MuiGrid-grid-xs-6')]"
    block_reports_xpath = "//main//div[3][contains(@class, 'MuiGrid-grid-xs-6')]"
    block_events_xpath = "//main//div[4][contains(@class, 'MuiGrid-grid-xs-6')]"
    add_player_button_xpath = "//a[contains(@href, '/players/add')]/button"
    dev_contact_link_xpath = "//a[contains(@href, 'https://app.slack.com/')]"
    logo_xpath = "//div[@title='Logo Scouts Panel']"
    main_header_xpath = "//main//h2[text()='Scouts Panel']"
    main_panel_text_xpath = "//main//p"
    last_cr_player_button_xpath = "//a[1][contains(@href, 'edit')]/button"
    last_upd_player_button_xpath = "//a[2][contains(@href, 'edit')]/button"
    last_cr_match_button_xpath = "//a[3][contains(@href, 'match')]/button"
    last_upd_match_button_xpath = "//a[4][contains(@href, 'match')]/button"
    last_upd_report_button_xpath = "//a[5][contains(@href, 'reports')]/button"






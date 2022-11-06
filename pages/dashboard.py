from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_menu_xpath = "//ul[1]/div[1]/span"
    players_menu_xpath = "//ul[1]/div[2]/span"
    language_menu_xpath = "//ul[2]/div[1]"
    sign_out_menu_xpath = "//ul[2]/div[2]"
    block_players_xpath = "//main//div[1][contains(@class, 'MuiGrid-grid-xs-6')]"
    block_matches_xpath = "//main//div[2][contains(@class, 'MuiGrid-grid-xs-6')]"
    block_reports_xpath = "//main//div[3][contains(@class, 'MuiGrid-grid-xs-6')]"
    block_events_xpath = "//main//div[4][contains(@class, 'MuiGrid-grid-xs-6')]"
    add_player_xpath = "//a[contains(@href, '/en/players/add')]"
    dev_contact_xpath = "//a[contains(@href, 'https://app.slack.com/client/T3X4CAKNU/C3XTEGXB6')]"
    logo_xpath = "//main/div[3]/div[1]/div/div[1]"
    main_header_xpath = "//main//h2[text()='Scouts Panel']"
    main_panel_text_xpath = "//main//p"
    last_created_player_xpath = "//a[1][contains(@href, 'edit')]"
    last_updated_player_xpath = "//a[2][contains(@href, 'edit')]"
    last_created_match_xpath = "//a[3][contains(@href, 'match')]"
    last_updated_match_xpath = "//a[4][contains(@href, 'match')]"
    last_updated_report_xpath = "//a[5][contains(@href, 'reports')]"






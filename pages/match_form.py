from pages.base_page import BasePage


class matchForm(BasePage):
    main_page_menu_xpath = "//ul[1]/div[1]/span",
    players_menu_xpath = "//ul[1]/div[2]/span",
    player_menu_xpath = "//ul[2]/div[1]/span",
    matches_menu_xpath = "//ul[2]/div[2]/span",
    reports_menu_xpath = "//ul[2]/div[3]/span",
    language_menu_xpath = "//ul[3]/div[1]/span",
    sign_out_menu_xpath = "//ul[3]/div[1]/span",
    page_title_xpath = "//div[contains(@class, 'MuiCardHeader-content')]",
    add_language_button_xpath = "//main//div[15]/button",
    add_link_button_xpath = "//main//div[19]/button",
    submit_button_xpath = "//*[@id='__next']//button[@type='submit']",
    clear_button_xpath = "//*[@id='__next']//form/div[3]/button[2]",
    email_input_xpath = "//*[@id='__next']//input[@name='email']",
    name_input_xpath = "//input[@name='name']",
    surname_input_xpath = "//input[@name='surname']",
    phone_input_xpath = "//input[@name='phone']",
    weight_select_xpath = "//input[@name='weight']",
    height_select_xpath = "//input[@name='height']",
    age_select_xpath = "//input[@name='age']",
    leg_select_xpath = "//input[@name='leg']",
    club_input_xpath = "//input[@name='club']",
    level_input_xpath = "//input[@name='level']",
    main_position_input_xpath = "//input[@name='mainPosition']",
    second_position_input_xpath = "//input[@name='secondPosition']",
    district_select_xpath = "//*[@id='district']",
    achievements_input_xpath = "//input[@name='achievements']",
    language_input_xpath = "//input[contains(@name='languages')]",
    remove_language_xpath = "",
    youtube_input_xpath = "",
    remove_youtube_xpath = "",
    ball_input_xpath = "",
    minut_90_input_xpath = "",
    facebook_input_xpath = "",





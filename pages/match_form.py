from pages.base_page import BasePage


class matchForm(BasePage):
    main_page_menu_xpath = '//span[text()="Main page" or  text()="Strona główna"]//ancestor::*[@role="button"]',
    players_menu_xpath = '//span[text()="Players" or text()="Gracze"]//ancestor::*[@role="button"]',
    player_menu_xpath = '//ul[2]/div[1]/span',
    matches_menu_xpath = '//ul[2]/div[2]/span',
    reports_menu_xpath = '//ul[2]/div[3]/span',
    language_menu_xpath = '//ul[3]/div[1]/span',
    sign_out_menu_xpath = '//ul[3]/div[1]/span',
    page_title_xpath = '//*[contains(@class, "Header-content")]',
    add_language_button_xpath = '//*[text()="Dodaj język" or text()="Add language"]',
    add_link_button_xpath = '//main//div[19]/button',
    submit_button_xpath = '//*[@type="submit"]',
    clear_button_xpath = '//form/div[3]/button[@type="button"]',
    email_input_xpath = '//*[@name="email"]',
    name_input_xpath = '//*[@name="name"]',
    surname_input_xpath = '//*[@name="surname"]',
    phone_input_xpath = '//*[@name="phone"]',
    weight_select_xpath = '//*[@name="weight"]',
    height_select_xpath = '//*[@name="height"]',
    age_select_xpath = '//*[@name="age"]',
    leg_select_xpath = '//*[@name="leg"]',
    club_input_xpath = '//*[@name="club"]',
    level_input_xpath = '//*[@name="level"]',
    main_position_input_xpath = '//*[@name="mainPosition"]',
    second_position_input_xpath = '//*[@name="secondPosition"]',
    district_select_xpath = '//*[@id="district"]',
    achievements_input_xpath = '//*[@name="achievements"]',
    language_input_xpath = '//input[contains(@name, "languages")]',
    remove_language_xpath = '//*[@title="Remove Language" or @title="Usuń język"]',
    youtube_input_xpath = '//*[contains(@name, "webYT")]',
    remove_youtube_xpath = '//button[contains(@title, "Youtube")]',
    minut_90_input_xpath = '//*[@name="web90"]',
    facebook_input_xpath = '//*[@name="webFB"]',





from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time


class Main_page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    #Locators
    search_bar = "//input[@type='search']"
    popup_not_allow = "moe-dontallow_button" #id
    view_all_button = "//div[@data-group='view-all']"
    word_to_assert = "boost-pfs-search-result-header" #class

    #Getters
    def get_search_bar(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.search_bar)))

    def get_popup_not_allow(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.ID, self.popup_not_allow)))

    def get_view_all_button(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.view_all_button)))

    def get_word_to_assert(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.word_to_assert)))

    #Actions
    def enter_query(self, query):
        self.get_search_bar().send_keys(query)
        print('The query has been entered')

    def close_popup(self):
        self.get_popup_not_allow().click()
        print('Popup closed')

    def click_to_view_all(self):
        self.get_view_all_button().click()
        print('Clicked to view all the results')

    #Methods
    def send_search_query(self, url, query):
        self.browser.get(url)
        self.browser.maximize_window()
        self.get_current_url()
        time.sleep(3)
        self.enter_query(query)
        self.click_to_view_all()
        self.assert_word(self.get_word_to_assert(), f'Search results for "{query}"')


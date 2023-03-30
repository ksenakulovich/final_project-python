from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time


class Filter_page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    #Locators
    filter_women = '//*[@id="boost-pfs-filter-tree-pf-t-section"]/div/ul/li[5]/button' #women
    filter_dresses = '//*[@id="boost-pfs-filter-tree-pf-t-category"]/div[2]/ul/li[6]/button' #dresses
    filter_size = '//*[@id="boost-pfs-filter-tree-pf-opt-size"]/div[2]/ul/li[2]/button' #medium size
    filter_price_above_60 = '//*[@id="boost-pfs-filter-tree-pf-p-price"]/div/ul/li[2]/button' #price above 60
    filter_black = '//*[@id="boost-pfs-filter-tree-pf-t-colour"]/div/ul/li[3]/span' #black color
    link_to_dress = '.full-unstyled-link'
    dress_price = '.price-item > span:nth-child(2)'
    dress_medium_size_button = 'fieldset > label:nth-child(6)'
    sorting_list = '.boost-pfs-filter-custom-sorting .facet-filters__sort'
    clear_filters_button = '//*[@id="boost-pfs-filter-tree"]/div/div[2]/div/div[1]/button'
    lowest_price_el = "//a[@href='/collections/all/products/green-socks-124180453']"

    #Getters
    def get_filter_women(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.filter_women)))

    def get_filter_dresses(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.filter_dresses)))

    def get_filter_size(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.filter_size)))

    def get_filter_price_above_60(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_above_60)))

    def get_filter_black(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.filter_black)))

    def get_link_to_dress(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.link_to_dress)))

    def get_clear_filters_button(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.clear_filters_button)))

    def get_sorting_list(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.sorting_list)))

    def get_lowest_price_el(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.lowest_price_el)))


    #Actions
    def check_filter_women(self):
        self.browser.execute_script("arguments[0].scrollIntoView();", self.get_filter_women())
        self.get_filter_women().click()
        time.sleep(3)
        print('Filter Women was clicked')

    def check_filter_dresses(self):
        self.browser.execute_script("arguments[0].scrollIntoView();", self.get_filter_dresses())
        self.get_filter_dresses().click()
        time.sleep(3)
        print('Filter Dresses was clicked')

    def check_filter_size(self):
        self.browser.execute_script("arguments[0].scrollIntoView();", self.get_filter_size())
        self.get_filter_size().click()
        time.sleep(3)
        print('Filter Size was clicked')

    def check_filter_price_above_60(self):
        self.browser.execute_script("arguments[0].scrollIntoView();", self.get_filter_price_above_60())
        self.get_filter_price_above_60().click()
        time.sleep(3)
        print('Filter Above SAR 60 was clicked')

    def check_get_filter_black(self):
        self.browser.execute_script("arguments[0].scrollIntoView();", self.get_filter_black())
        self.get_filter_black().click()
        time.sleep(3)
        print('Filter Black was clicked')

    def click_link_to_dress(self):
        self.browser.execute_script("arguments[0].scrollIntoView();", self.get_link_to_dress())
        self.get_link_to_dress().click()
        print('Scrolled to link and clicked')

    def click_clear_filters_button(self):
        self.browser.execute_script("arguments[0].scrollIntoView();", self.get_clear_filters_button())
        self.get_clear_filters_button().click()
        print('Filters cleared')

    def click_sorting_list(self):
        self.browser.execute_script("arguments[0].scrollIntoView();", self.get_sorting_list())
        self.get_sorting_list().click()
        print('Sorting list clicked')

    def click_lowest_price_element(self):
        self.browser.execute_script("arguments[0].scrollIntoView();", self.get_lowest_price_el())
        self.get_lowest_price_el().click()
        time.sleep(3)
        print('LP element opened')

    # Methods
    def filter_dress(self):
        self.get_current_url()
        self.check_filter_women()
        self.check_filter_dresses()
        self.check_filter_size()
        self.check_filter_price_above_60()
        self.check_get_filter_black()
        self.click_link_to_dress()
        assert self.browser.current_url == 'https://sa.redtagfashion.com/products/black-dresses-125035021', 'You are on the wrong page'

    def open_lowest_price_el(self):
        self.get_current_url()
        self.click_sorting_list()
        self.get_sorting_list().send_keys(Keys.DOWN)
        self.get_sorting_list().send_keys(Keys.RETURN)
        self.click_lowest_price_element()











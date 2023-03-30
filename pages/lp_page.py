from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time


class Lp_page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    #Locators
    lp_price = '.price-item > span:nth-child(2)'
    lp_lxl_size_button = 'fieldset > label:nth-child(6)'
    add_to_cart_button = '//button[@name="add"]'
    lp_name = 'div > .product__title'

    # Getters
    def get_lp_price(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.lp_price)))

    def get_lp_lxl_size_button(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.lp_lxl_size_button)))

    def get_to_cart_button(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_item_name(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.lp_name)))

    # Actions
    def get_price_as_variable(self):
        dress_price_on_page = self.get_lp_price().text.strip(' ')
        print('Dress price from page saved')
        return dress_price_on_page

    def get_item_name_as_variable(self):
        it_name_on_page = self.get_item_name().text.strip(' ')
        print('Item name from page saved')
        return it_name_on_page

    def click_medium_size_button(self):
        self.get_lp_lxl_size_button().click()
        time.sleep(3)
        print('Medium size clicked')

    def click_to_cart_button(self):
        self.browser.execute_script("arguments[0].scrollIntoView();", self.get_to_cart_button())
        self.get_to_cart_button().click()
        time.sleep(3)
        print('Added to cart')

    # Methods
    def select_dress(self):
        self.get_current_url()
        self.click_medium_size_button()
        self.click_to_cart_button()
        print('Item price: ' + self.get_price_as_variable(), 'Item name: ' + self.get_item_name_as_variable())

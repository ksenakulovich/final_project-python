from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time


class Item_page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    #Locators
    item_price = '.price-item > span:nth-child(2)'
    item_medium_size_button = 'fieldset > label:nth-child(6)'
    add_to_cart_button = '//button[@name="add"]'
    item_name = 'div > .product__title'

    # Getters
    def get_item_price(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.item_price)))

    def get_medium_size_button(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.item_medium_size_button)))

    def get_to_cart_button(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_item_name(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.item_name)))

    # Actions
    def get_price_as_variable(self):
        item_price_on_page = self.get_item_price().text.strip(' ')
        print('Item price from page saved')
        return item_price_on_page

    def get_item_name_as_variable(self):
        it_name_on_page = self.get_item_name().text.strip(' ')
        print('Item name from page saved')
        return it_name_on_page

    def click_medium_size_button(self):
        self.get_medium_size_button().click()
        print('Medium size clicked')

    def click_to_cart_button(self):
        self.browser.execute_script("arguments[0].scrollIntoView();", self.get_to_cart_button())
        self.get_to_cart_button().click()
        print('Added to cart')

    # Methods
    def select_item(self):
        self.get_current_url()
        self.click_medium_size_button()
        self.click_to_cart_button()
        print('Item price: ' + self.get_price_as_variable(), 'Item name: ' + self.get_item_name_as_variable())






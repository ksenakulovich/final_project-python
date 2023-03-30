from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Cart_page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    #Locators
    cart_icon = '.header__icon--cart'
    cart_item_price = '.item-current-price'
    cart_item_name = '.item-name'
    cart_size = 'p.item-size > span:nth-child(2)'
    remove_button_for_second_item = '//cart-remove-button[@id="Remove-2"]'
    cart_increase_number = 'div.quantity-container > quantity-input > button.shopping-bag-plus'
    checkout_button = '//button[@id="checkout"]'
    item_desc_checkout = '.product__description__name'
    item_price_checkout = '.product__price .order-summary__emphasis'

    # Getters
    def get_cart_icon(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.cart_icon)))

    def get_cart_item_price(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.cart_item_price)))

    def get_cart_item_name(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.cart_item_name)))

    def get_cart_size(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.cart_size)))

    def get_remove_button_for_second_item(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.remove_button_for_second_item)))

    def get_cart_increase_number(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.cart_increase_number)))

    def get_checkout_button(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_item_desc_checkout(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.item_desc_checkout)))

    def get_item_price_checkout(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.item_price_checkout)))

    #Actions
    def click_cart_icon(self):
        self.get_cart_icon().click()
        print('Cart icon clicked')

    def click_remove_button_for_second_item(self):
        self.get_remove_button_for_second_item().click()
        print('Remove button clicked')

    def click_cart_increase_number(self):
        self.get_cart_increase_number().click()
        print('Number of items was increased')

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Proceeded to checkout')

    def get_final_name_as_variable(self):
        item_name_fin = self.get_item_desc_checkout().text
        print('Final name saved')
        return item_name_fin

    def get_final_price_as_variable(self):
        item_price_fin = self.get_item_price_checkout().text.strip('SAR')
        print('Final price saved')
        return item_price_fin

    #Methods
    def delete_second_from_cart(self):
        self.get_current_url()
        self.click_cart_icon()
        self.click_remove_button_for_second_item()






















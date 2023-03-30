from selenium import webdriver
from pages.cart_page import Cart_page
from pages.item_page import Item_page
from pages.main_page import Main_page
from pages.filter_page import Filter_page

url_women = 'https://sa.redtagfashion.com/pages/women'
first_item = 'dress'
second_item = 'skirt'


def test_women_clothes_workflow():
    browser = webdriver.Chrome()
    test_page_dress = Main_page(browser)
    test_page_dress.send_search_query(url_women, first_item) #вводим первый запрос на платье

    filtering_1 = Filter_page(browser)
    filtering_1.filter_dress() #фильтрация по ряду параметров

    dress = Item_page(browser)
    dress.select_item() #добавление платья в корзину
    browser.back()
    filtering_1.click_clear_filters_button() #сбрасываем фильтры по умолчанию

    test_page_skirt = Main_page(browser)
    test_page_skirt.send_search_query(url_women, second_item) #вводим второй запрос

    filtering_2 = Filter_page(browser)
    filtering_2.open_lowest_price_el() #выбираем элемент, который будет самм первым при сортировке по наименьшей цене при помощи дропдауна

    lp = Item_page(browser)
    lp.select_item() #второй товар в корзине
    name = lp.get_item_name_as_variable() #сохраняем наименование для проверки
    price = lp.get_price_as_variable() #сохраняем цену для проверки

    cart_p = Cart_page(browser)
    cart_p.delete_second_from_cart() #удаляем товар, добавленный первым, из корзины
    cart_p.click_cart_increase_number() #увеличиваем кол-во оставшегося товара на 1
    cart_p.click_checkout_button()
    assert name == cart_p.get_final_name_as_variable(), 'Item names do not match' #сравнение наименования при добавлении в корзину и при оплате
    print('Item names match')
    assert str((float(price) * 2)) + '0' == cart_p.get_final_price_as_variable(), 'Item prices do not match' #сравнение цены при добавлении в корзину и при оплате (умножаем на два, поскольку кол-во товара было увеличено)
    print('Item price match')
    cart_p.get_screenshot()


#Запуск тестов
test_women_clothes_workflow()

В данном репозитории располагается финальный проект, который является последним заданием курса https://stepik.org/course/120491/syllabus. Для данного проекта мною был выбран сайт одежды https://sa.redtagfashion.com/, а именно его женская секция https://sa.redtagfashion.com/pages/women. Суть проекта - описать путь покупателя от захода на сайт до страницы оплаты, при этом при выборе товара следует применить фильтрацию (весь флоу должен быть по возможности усложнённым).

Тест, написанный в моём проекте, проходит следующие шаги:
1. Заход на сайт, ввод в поисковую строку слова "dress".
2. Отфильтровываем полученные результаты при помощи фильтров сбоку. Применяются следующие фильтры: "Women", "Dresses", "Medium", "Above SAR 60", "Black". На момент написания проекта такая фильтрация выдавала одно платье.
3. Добавление платья в корзину.
4. Возврат на главную страницу женской секции, сброс всех фильтров.
5. Ввод второго запроса ("skirt").
6. В этот раз используем выпадающий список для сортировки, где выбираем "сортировка по наименьшей цене".
7. Добавление самого дешёвого товара в корзину (он будет первым после сортировки), сохранение его цены и наименования в переменные для последующего сравнения.
8. Переход в корзину (боковое выезжающее меню). После перехода удаляем товар, добавленным первым в корзину (платье), а количество второго товара (того, что самый дешёвый), увеличиваем на +1.
9. Переход на страницу оплаты и сравнение цены и наименования, отображаемого на странице оплаты, с теми, что были сохранены ранее.
10. Скриншот последней страницы.

На момент финальной проверки перед загрузкой проекта на GitHub, вывод консоли выглядел так:

Testing started at 14:44 ...
Launching pytest with arguments test_flow.py --no-header --no-summary -q in C:\Users\User\PycharmProjects\pythonProject\tests

============================= test session starts =============================
collecting ... collected 1 item

test_flow.py::test_women_clothes_workflow PASSED                         [100%]Current URL:https://sa.redtagfashion.com/pages/women
The query has been entered
Clicked to view all the results
Good value word
Current URL:https://sa.redtagfashion.com/search?q=dress
Filter Women was clicked
Filter Dresses was clicked
Filter Size was clicked
Filter Above SAR 60 was clicked
Filter Black was clicked
Scrolled to link and clicked
Current URL:https://sa.redtagfashion.com/products/black-dresses-125035021
Medium size clicked
Added to cart
Item price from page saved
Item name from page saved
Item price: 69.00 Item name: Women Black Front Button Body Cone Dress
Filters cleared
Current URL:https://sa.redtagfashion.com/pages/women
The query has been entered
Clicked to view all the results
Good value word
Current URL:https://sa.redtagfashion.com/search?q=skirt
Sorting list clicked
LP element opened
Current URL:https://sa.redtagfashion.com/products/green-socks-124180453
Medium size clicked
Added to cart
Item price from page saved
Item name from page saved
Item price: 10.00 Item name: Senior Girls White and Green Stripes Full Length Socks
Item name from page saved
Item price from page saved
Current URL:https://sa.redtagfashion.com/products/green-socks-124180453?variant=44482482077942
Cart icon clicked
Remove button clicked
Number of items was increased
Proceeded to checkout
Final name saved
Item names match
Final price saved
Item price match


======================== 1 passed in 125.81s (0:02:05) ========================

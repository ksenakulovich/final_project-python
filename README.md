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

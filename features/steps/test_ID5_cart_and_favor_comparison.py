# -*- coding: utf-8 -*-
import time

from behave import given, when, then
from features import environment
from faker import Faker

fake = Faker()


@given(u'пользователь открывает сайт')
def id_test5_7(self):
    """
    Строка 7
    """
    page = environment.get_page(self)
    page.goto("https://stroyseven.ru/compare-products/")


@given(u'нажимает кнопку "Личный кабинет"')
def id_test5_8(self):
    """
    Строка 8
    """
    self.page.get_by_label("Login Register").click()


@given(u'в поля emal и пароль вводит валидные данные')
def id_test5_9(self):
    """
    Строка 9
    """
    self.page.get_by_placeholder("E-Mail", exact=True).click()
    self.page.get_by_placeholder("E-Mail", exact=True).fill("tetst79@mail.ru")
    self.page.get_by_placeholder("Пароль").click()
    self.page.get_by_placeholder("Пароль").fill("141009вы")


@given(u'нажимает кнопку "Войти"')
def id_test5_10(self):
    """
    Строка 10
    """
    self.page.get_by_role("button", name="Войти").click()


@when(u'пользователь нажал кнопку "Каталог"')
def id_test5_13_45(self):
    """
    Строка 13,45
    """
    self.page.get_by_label("Catalog").click()


@when(u'в выпадающем списке выбрал "Блоки строительные"')
def id_test5_15(self):
    """
    Строка 15
    """
    self.page.get_by_role("link", name="Блоки строительные Блоки строительные").click()


@when(u'в фильтре выбрал производителя "гипсополимер"')
def id_test5_16(self):
    """
    Строка 16
    """
    self.page.get_by_role("button", name="Гипсополимер").click()


@when(u'в выпадающей сноске нажал на кнопку "Показать 6 товаров"')
def id_test5_17(self):
    """
    Строка 17
    """
    self.page.get_by_role("button", name="Показать 6 товаров").first.click()


@when(u'он нажал на рисунок с корзиной на окошке одного товара')
def id_test5_18(self):
    """
    Строка 18
    """
    self.page.locator("button").filter(has_text="Купить").first.click()


@then(u'появилось сообщение о добавлении этого товара в корзину')
def id_test5_19_21_23(self):
    """
    Строка 19,21,23
    """
    self.page.get_by_role("button", name="×").click()


@when(u'он нажал на рисунок с корзиной на окошке другого товара')
def id_test5_20(self):
    """
    Строка 20
    """
    self.page.locator("button").filter(has_text="Купить").nth(1).click()


@when(u'он нажал на рисунок с корзиной на окошке третьего товара')
def id_test5_22(self):
    """
    Строка 22
    """
    self.page.locator("button").filter(has_text="Купить").nth(1).click()


@when(u'пользователь нажал кнопку "Корзина"')
def id_test5_24_28(self):
    """
    Строка 24,28
    """
    self.page.get_by_role("button", name="Корзина").click()


@then(u'открылась шторка корзины с количеством 3 и их ценой')
def id_test5_25_29(self):
    """
    Строка 25,29
    """
    self.page.get_by_role("textbox").nth(1).click()
    self.page.get_by_role("textbox").nth(2).click()
    self.page.get_by_role("textbox").nth(3).click()


@when(u'пользователь нажал кнопку "Оформление заказа"')
def id_test5_26(self):
    """
    Строка 26
    """
    self.page.get_by_role("link", name="Оформить заказ").click()


@then(u'открылась страница Оформление заказа')
def id_test5_27(self):
    """
    Строка 27
    """
    self.page.get_by_role("heading", name="Оформление заказа").click()


@when(u'пользователь нажал кнопку "Удалить" на окошке одного товара')
def id_test5_30(self):
    """
    Строка 30
    """
    self.page.get_by_role("button", name="").first.click()


@then(u'в корзине изменилось количество товаров с 3 на 2 и изменилась цена')
def id_test5_31(self):
    """
    Строка 31
    """
    self.page.get_by_role("textbox").nth(1).click()
    self.page.get_by_role("textbox").nth(2).click()


@when(u'пользователь нажал кнопку "Удалить" на окошке другого товара')
def id_test5_32(self):
    """
    Строка 32
    """
    self.page.get_by_role("button", name="").first.click()


@then(u'в корзине изменилось количество товаров с 2 на 1 и изменилась цена')
def id_test5_33(self):
    """
    Строка 33
    """
    self.page.locator("#cart").get_by_role("textbox").click()


@when(u'пользователь нажал кнопку "Удалить" на последнего товара')
def id_test5_34(self):
    """
    Строка 34
    """
    self.page.get_by_role("button", name="").first.click()


@then(u'в корзине не осталось товаров')
def id_test5_35(self):
    """
    Строка 35
    """
    self.page.locator("#cart").get_by_text("Ваша корзина пуста!").click()


@when(u'закрыл шторку "Корзины" стрелкой')
def id_test5_36(self):
    """
    Строка 36
    """
    self.page.locator("#cart").get_by_role("button").nth(1).click()


@when(u'нажал на кнопку "Кабинет"')
def id_test5_37_65(self):
    """
    Строка 37,65
    """
    self.page.get_by_label("Login Register").click()


@when(u'выбрал позицию "Выйти"')
def id_test5_38_66(self):
    """
    Строка 38,66
    """
    self.page.get_by_role("link", name="Выход").click()


@then(u'он перешел на страницу "logout"')
def id_test5_39_67(self):
    """
    Строка 39,67
    """
    self.page.get_by_role("heading", name="Выход").click()


@when(u'он нажал на кнопку "Корзина"')
def id_test5_40(self):
    """
    Строка 40
    """
    self.page.get_by_role("button", name="Корзина").click()


@then(u'открылась шторка "Корзины" с надписью "Ваша корзина пуста!"')
def id_test5_41(self):
    """
    Строка 41
    """
    self.page.get_by_text("Ваша корзина пуста!").click()


@when(u'в выпадающем списке выбрал "Листовые материалы"')
def id_test5_46(self):
    """
    Строка 46
    """
    self.page.get_by_role("link", name="Листовые материалы Листовые материалы").click()


@when(u'в фильтре выбрал производителя "Германия"')
def id_test5_47(self):
    """
    Строка 47
    """
    self.page.get_by_role("button", name="Германия").click()


@when(u'в выпадающей сноске нажал на кнопку "Показать 13 товаров"')
def id_test5_48(self):
    """
    Строка 48
    """
    self.page.get_by_role("button", name="Показать 13 товаров").first.click()


@when(u'он нажал на рисунок с сердцем на окошке одного товара')
def id_test5_49(self):
    """
    Строка 49
    """
    self.page.locator(".stock-status").first.hover()
    self.page.locator(".wishlist > .btn").first.click()


@then(u'появилось сообщение о добавлении этого товара в избранном')
def id_test5_50_52_54(self):
    """
    Строка 50,52,54
    """
    self.page.get_by_text("×").click()


@when(u'он нажал на рисунок с сердцем на окошке другого товара')
def id_test5_51(self):
    """
    Строка 51
    """
    self.page.locator("div:nth-child(2) > .product-thumb > .caption > .ch-stock-status > .stock-status").hover()
    self.page.locator("div:nth-child(2) > .product-thumb > .image > .addit-action > .wishlist > .btn").click()


@when(u'он нажал на рисунок с сердцем на окошке третьего товара')
def id_test5_53(self):
    """
    Строка 53
    """
    self.page.locator("div:nth-child(3) > .product-thumb > .caption > .ch-stock-status > .stock-status").hover()
    self.page.locator("div:nth-child(3) > .product-thumb > .image > .addit-action > .wishlist > .btn").click()


@when(u'пользователь нажал кнопку "Избранное"')
def id_test5_55(self):
    """
    Строка 55
    """
    self.page.get_by_role("link", name="Избранное").click()


@then(u'открылась страница избранного с количеством 3 и их ценами')
def id_test5_56_60(self):
    """
    Строка 56,60
    """
    self.page.get_by_role("heading", name="Избранное").click()


@when(u'пользователь в блоке"Наличие товаров" выбрал кнопку "Нет в наличии"')
def id_test5_57(self):
    """
    Строка 57
    """
    self.page.get_by_text("Нет в наличии").click()


@then(u'все выбранные товары скрылись')
def id_test5_58(self):
    """
    Строка 58
    """
    self.page.get_by_text("Избранное пусто").click()


@when(u'пользователь в блоке"Наличие товаров" выбрал кнопку "В наличии"')
def id_test5_59(self):
    """
    Строка 59
    """
    self.page.get_by_text("В наличии", exact=True).click()


@when(u'пользователь нажал кнопку "Сердечко с галочкой" на окошке одного товара')
def id_test5_61(self):
    """
    Строка 61
    """
    self.page.get_by_text("В наличии").nth(2).hover()
    self.page.get_by_role("button", name="Удалить из закладок").first.click()


@then(u'появилось сообщении об удалении данного товара из избранного')
def id_test5_62_64(self):
    """
    Строка 62,64
    """
    self.page.get_by_text("×").click()


@then(u'открылась страница "Избранного" с надписью "Избранное пусто"')
def id_test5_69(self):
    """
    Строка 69
    """
    self.expect(self.page.get_by_text("Избранное пусто")).to_be_visible()












##############################################


@when(u'пользователь вводит случайный адрес')
def id_test4_10(self):
    """
    Строка 10
    """
    self.page.get_by_placeholder("Адрес", exact=True).click()
    self.page.get_by_placeholder("Адрес", exact=True).fill("м")
    self.page.get_by_text("г Москва").click()


@when(u'вводит случайный вес товара')
def id_test4_11(self):
    """
    Строка 11
    """
    self.page.get_by_placeholder("Укажите вес заказа, кг").click()
    self.page.get_by_placeholder("Укажите вес заказа, кг").fill("56")
    self.page.get_by_placeholder("Укажите вес заказа, кг").press("Enter")


@when(u'вводит случайный обЪем товара')
def id_test4_12(self):
    """
    Строка 12
    """
    self.page.get_by_placeholder("Укажите объем заказа, м").click()
    self.page.get_by_placeholder("Укажите объем заказа, м").fill("5")
    self.page.get_by_placeholder("Укажите объем заказа, м").press("Enter")


@then(u'в поле "Расчетная стоимость" появиться некая цена')
def id_test4_13(self):
    """
    Строка 13
    """
    pass


@when(u'в блоке срока доставки поменять значение радиокнопки')
def id_test4_14(self):
    """
    Строка 14
    """
    self.page.get_by_label("Точно ко времени").check()


@then(u'в поле "Расчетная стоимость" цена изменится')
def id_test4_15_17_19_21_23_25(self):
    """
    Строка 15,17,19,21,23,25
    """
    pass


@when(u'в блоке способ разгрузки поменять значение радиокнопки')
def id_test4_16(self):
    """
    Строка 16
    """
    self.page.get_by_label("Разгрузка без проноса (до 20").check()


@when(u'в блоке Разгрузка манипулятором установить флажок')
def id_test4_18(self):
    """
    Строка 18
    """
    self.page.get_by_label("Разгрузка манипулятором").check()


@when(u'в блоке Подъем на этаж установить флажок')
def id_test4_20(self):
    """
    Строка 20
    """
    self.page.get_by_label("Подъем на этаж").check()


@when(u'в поле "Укажите номер этажа" изменить значение')
def id_test4_22(self):
    """
    Строка 22
    """
    self.page.get_by_label("Укажите номер этажа").fill("4")
    self.page.get_by_label("Укажите номер этажа").press("Enter")


@when(u'в блоке "Тип подъема на этаж" поменять значение радиокнопки')
def id_test4_24(self):
    """
    Строка 24
    """
    self.page.get_by_label("Без лифта").check()

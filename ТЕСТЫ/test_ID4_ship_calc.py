# -*- coding: utf-8 -*-
import time

from behave import given, when, then
from features import environment
from faker import Faker

fake = Faker()


@given(u'пользователь открывает сайт')
def id_test3_6(self):
    """
    Строка 6
    """
    page = environment.get_page(self)
    page.goto("https://stroyseven.ru/compare-products/")


@given(u'нажимает кнопку "Калькулятор доставки"')
def id_test4_7(self):
    """
    Строка 7
    """
    self.page.get_by_role("button", name=" Калькулятор доставки").click()


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
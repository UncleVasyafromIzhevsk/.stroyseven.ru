# -*- coding: utf-8 -*-
import time

from behave import given, when, then
from features import environment
from faker import Faker

fake = Faker()


@given(u'пользователь открывает сайт')
def id_test3_7(self):
    """
    Строка 7
    """
    page = environment.get_page(self)
    page.goto("https://stroyseven.ru/compare-products/")


@given(u'нажимает кнопку "Личный кабинет"')
def id_test3_8(self):
    """
    Строка 8
    """
    self.page.get_by_label("Login Register").click()


@given(u'нажимает кнопку "Регистрация"')
def click_btn_reg(self):
    """
    Строка 9
    """
    self.page.get_by_role("button", name="Регистрация").click()


@when(u'в модальном окне emal и пароль ввести случайно сгенерированные данные')
def id_test3_12(self):
    """
    Строка 12
    """
    self.page.get_by_placeholder("E-Mail", exact=True).click()
    self.page.get_by_placeholder("E-Mail", exact=True).fill(fake.email())
    self.page.get_by_placeholder("Пароль").click()
    self.page.get_by_placeholder("Пароль").fill(fake.password())


@when(u'пользователь нажмет кнопку "Войти"')
def id_test3_13_18_28(self):
    """
    Строка 13,18,28
    """
    self.page.get_by_role("button", name="Войти").click()


@then(u'появиться предупреждение "Ошибка: Неправильный E-Mail и/или пароль."')
def id_test3_14(self):
    """
    Строка 14
    """
    self.page.get_by_text("Ошибка: Неправильный E-Mail").click()


@when(u'в модальном окне emal и пароль ввести валидные данные')
def id_test3_17_27(self):
    """
    Строка 17,27
    """
    self.page.get_by_placeholder("E-Mail", exact=True).click()
    self.page.get_by_placeholder("E-Mail", exact=True).fill("tetst79@mail.ru")
    self.page.get_by_placeholder("Пароль").click()
    self.page.get_by_placeholder("Пароль").fill("141009вы")


@then(u'откроется стартовая страница')
def id_test3_19_29(self):
    """
    Строка 19,29
    """
    self.page.get_by_role("heading", name="Сравнение товаров").click()


@when(u'пользователь нажимает кнопку "Личный кабинет"')
def id_test3_20_30(self):
    """
    Строка 20,30
    """
    self.page.get_by_label("Login Register").click()


@when(u'пользователь в выпадающем списке выберет пункт "Личный кабинет"')
def id_test3_21_31(self):
    """
    Строка 21,31
    """
    self.page.get_by_role("link", name="Личный кабинет", exact=True).click()


@then(u'откроется страница "my-account"')
def id_test3_22_32(self):
    """
    Строка 22,32
    """
    self.page.get_by_role("heading", name="Моя учетная запись").click()


@when(u'пользователь в "Личный кабинет" нажмет кнопку "Выход"')
def id_test3_23(self):
    """
    Строка 23
    """
    self.page.get_by_role("link", name="Выход").click()


@then(u'откроется страница "logout"')
def id_test3_24(self):
    """
    Строка 24
    """
    self.page.get_by_role("heading", name="Выход").click()
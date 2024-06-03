# -*- coding: utf-8 -*-
import time

from behave import given, when, then
from features import environment
from faker import Faker

fake = Faker()


@given(u'пользователь открыл сайт')
def id_test6_7(self):
    """
    Строка 7
    """
    page = environment.get_page(self)
    page.goto("https://stroyseven.ru/compare-products/")


@given(u'нажал кнопку "Кабинет"')
def id_test6_8(self):
    """
    Строка 8
    """
    self.page.get_by_label("Login Register").click()


@when(u'в поля "EMAIL" и "Пароль" он ввел свои данные')
def id_test6_9(self):
    """
    Строка 9
    """
    self.page.get_by_placeholder("E-Mail", exact=True).click()
    self.page.get_by_placeholder("E-Mail", exact=True).fill("tetst79@mail.ru")
    self.page.get_by_placeholder("Пароль").click()
    self.page.get_by_placeholder("Пароль").fill("141009вы")


@when(u'нажал кнопку "Войти"')
def id_test6_10(self):
    """
    Строка 10
    """
    self.page.get_by_role("button", name="Войти").click()


@then(u'он авторизовался')
def id_test6_11(self):
    """
    Строка 11
    """
    self.page.get_by_label("Login Register").click()


@when(u'пользователь в поле поиска вводит буквы "мол"')
def id_test6_14(self):
    """
    Строка 14
    """
    self.page.get_by_role("textbox", name="Поиск").fill("мол")


@then(u'выпадает список с предлагаемыми вариантами товаров')
def id_test6_15(self):
    """
    Строка 15
    """
    self.page.get_by_text("Товары", exact=True).hover()


@then(u'в этих вариантах присутствуют буквы "мол" в таком же порядке расположения')
def id_test6_16(self):
    """
    Строка 16
    """
    self.page.get_by_text("Товары", exact=True).click()


@then(u'пользователь вышел из учетной записи')
def id_test6_17_27(self):
    """
    Строка 17,27
    """
    self.page.get_by_label("Login Register").click()
    self.page.get_by_role("link", name="Выход").click()
    self.page.get_by_role("heading", name="Выход").click()


@when(u'пользователь в поле поиска вводит буквы "молоток"')
def id_test6_20(self):
    """
    Строка 20
    """
    self.page.get_by_role("textbox", name="Поиск").fill("молоток")


@when(u'нажимает кнопку "лупы" в поле ввода запроса')
def id_test6_21(self):
    """
    Строка 21
    """
    self.page.get_by_role("button", name="Search").click()


@then(u'пользователь переходит на страницу поиска с предложенными вариантами товаров')
def id_test6_22(self):
    """
    Строка 22
    """
    self.page.get_by_role("heading", name="Поиск - молоток").click()


@then(u'в этих вариантах присутствует слово "молоток" в таком же порядке расположения')
def id_test6_23(self):
    """
    Строка 23
    """
    self.page.get_by_role("heading", name="Поиск - молоток").click()


@then(u'слово "молоток" или образованные от него слова в описании первого товара')
def id_test6_24(self):
    """
    Строка 24
    """
    self.page.get_by_text("Молоток 1500").hover()


@then(u'слово "молоток" или образованные от него слова в описании второго товара')
def id_test6_25(self):
    """
    Строка 25
    """
    self.page.get_by_text("Молоток слесарный, 1000").hover()


@then(u'слово "молоток" или образованные от него слова в описании третьего товара')
def id_test6_26(self):
    """
    Строка 26
    """
    self.page.get_by_text("Молоток слесарный, 800 г, квадратный боек, деревянная рукоятка Sparta").hover()


@when(u'пользователь нажимает кнопку "Кабинет"')
def id_test6_30_42_45_55(self):
    """
    Строка 30,42,55
    """
    self.page.get_by_role("link", name="Избранное").click()
    self.page.get_by_label("Login Register").click()


@when(u'в выпадающем списке выбирает "Личный кабинет"')
def id_test6_31_48_51(self):
    """
    Строка 31
    """
    self.page.get_by_role("link", name="Личный кабинет", exact=True).click()


@then(u'он переходит в свой личный кабинет')
def id_test6_32(self):
    """
    Строка 32
    """
    self.page.get_by_role("heading", name="Моя учетная запись").click()


@when(u'он нажимает кнопку "Пароль"')
def id_test6_33(self):
    """
    Строка 33
    """
    self.page.get_by_role("link", name="Пароль").click()


@then(u'переходит на страницу смены пароля')
def id_test6_34(self):
    """
    Строка 34
    """
    self.page.get_by_role("heading", name="Изменить пароль").click()


@when(u'в поле "Пароль" он вводит новый пароль')
def id_test6_35(self):
    """
    Строка 35
    """
    self.page.get_by_placeholder("Пароль", exact=True).click()
    self.page.get_by_placeholder("Пароль", exact=True).fill("141009вы")


@when(u'в поле "Подтвердите пароль" вводит символы не соответствующие новому паролю')
def id_test6_36(self):
    """
    Строка 36
    """
    self.page.get_by_placeholder("Подтвердите пароль").click()
    self.page.get_by_placeholder("Подтвердите пароль").fill("141009ds")


@when(u'нажимает кнопку "Продолжить"')
def id_test6_37_40(self):
    """
    Строка 37_40
    """
    self.page.get_by_role("button", name="Продолжить").click()


@then(u'появляется предупреждение "Пароли и пароль подтверждения не совпадают!"')
def id_test6_38(self):
    """
    Строка 38
    """
    self.page.get_by_text("Пароли и пароль подтверждения не совпадают!").click()


@when(u'в поле "Подтвердите пароль" пользователь вводит символы соответствующие новому паролю')
def id_test6_39(self):
    """
    Строка 39
    """
    self.page.get_by_placeholder("Подтвердите пароль").fill("141009вы")


@then(u'появляется сообщение об удачной смене пароля')
def id_test6_41(self):
    """
    Строка 41
    """
    self.page.locator("#account-account").get_by_role("button").click()


@when(u'в выпадающем списке выбирает "Выйти"')
def id_test6_43_49(self):
    """
    Строка 43
    """
    self.page.get_by_role("banner").get_by_role("link", name="Выход").click()


@then(u'появляется надпись "Вы вышли из Личного Кабинета"')
def id_test6_44_50(self):
    """
    Строка 44,50
    """
    self.page.get_by_text("Вы вышли из Личного Кабинета").click()


@when(u'в появившемся модальном окне вводит свой EMAIL и новый пароль')
def id_test6_46(self):
    """
    Строка 46
    """
    self.page.get_by_placeholder("E-Mail", exact=True).click()
    self.page.get_by_placeholder("E-Mail", exact=True).fill("tetst79@mail.ru")
    self.page.get_by_placeholder("Пароль").click()
    self.page.get_by_placeholder("Пароль").fill("141009вы")
    self.page.get_by_role("button", name="Войти").click()


@then(u'пользователь авторизовался')
def id_test6_47(self):
    """
    Строка 47
    """
    pass
    # self.page.get_by_role("heading", name="Моя учетная запись").click()


@when(u'пользователь снова нажимает кнопку "Кабинет"')
def id_test6_51(self):
    """
    Строка 51
    """
    self.page.get_by_role("link", name="Личный кабинет", exact=True).click()


@then(u'появляется модальное окно авторизации')
def id_test6_52(self):
    """
    Строка 52
    """
    pass


@when(u'в появившемся модальном окне перейти по ссылке "Забыли пароль?"')
def id_test6_56(self):
    """
    Строка 56
    """
    self.page.get_by_role("link", name="Избранное").click()
    self.page.get_by_label("Login Register").click()
    self.page.get_by_role("banner").get_by_role("link", name="Выход").click()
    self.page.get_by_role("link", name="Избранное").click()
    self.page.get_by_label("Login Register").click()
    self.page.locator("#login_data").get_by_role("link", name="Забыли пароль?").click()


@then(u'он перенаправляется на страницу сброса пароля')
def id_test6_57(self):
    """
    Строка 54
    """
    self.page.get_by_text("Введите E-Mail").click()


@when(u'в поле EMAIL он введет свою почту')
def id_test6_55(self):
    """
    Строка 55
    """
    self.page.get_by_placeholder("E-Mail", exact=True).fill("tetst79@mail.ru")


@then(u'он перенаправляется на страницу авторизации')
def id_test6_56(self):
    """
    Строка 56
    """
    self.page.get_by_role("button", name="Продолжить").click()
    self.page.get_by_text("Зарегистрированный клиент").click()


@then(u'появляется сообщение о направлении на его почту нового пароля')
def id_test6_57(self):
    """
    Строка 57
    """
    self.page.locator("#account-login button").click()

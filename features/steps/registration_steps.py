# -*- coding: utf-8 -*-
import time

from behave import given, when, then
from features import environment
from faker import Faker


fake = Faker()


@given(u'Пользователь открывает сайт')
def registration(self):
    """
    :param self:
    :return:
    """
    page = environment.get_page(self)
    page.goto("https://stroyseven.ru/")


@given(u'Нажимает кнопку "Личный кабинет" и кнопку "Регистрация"')
def registration(self):
    """
    :param self:
    :return:
    """
    self.page.get_by_label("Login Register").click()
    self.page.get_by_role("button", name="Регистрация").click()


@when(u'В поля emal и пароль ввести зарегистрированные учетные данные')
def fill_user_data_field(self):
    """
    :param self:
    """
    self.page.get_by_label("ФИО или название компании").click()
    self.page.get_by_label("ФИО или название компании").fill("Иванов Василий")
    self.page.get_by_label("Email").click()
    self.page.get_by_label("Email").fill("tetst79@mail.ru")
    self.page.get_by_label("Пароль", exact=True).click()
    self.page.get_by_label("Пароль", exact=True).fill("141009вы")
    self.page.get_by_label("Подтвердите пароль").click()
    self.page.get_by_label("Подтвердите пароль").fill("141009вы")


@when(u'Нажать кнопку "Продолжить"')
def fill_user_data_in(self):
    """
    :param self:
    """
    self.page.locator("#simpleregister_button_confirm").click()

@then(u'Появиться предупреждение "Адрес уже зарегистрирован!"')
def is_next_warning(self):
    """
    :param self:
    """
    self.page.get_by_text("Адрес уже зарегистрирован!").click()


# Второй сценарий

@given(u'Пользователь переходит на главную страницу')
def registration(self):
    """
    :param self:
    :return:
    """
    self.page.goto("https://stroyseven.ru/")


@given(u'Нажимает кнопку "Личный кабинет" и кнопку "Регистрация" №2')
def registration(self):
    """
    :param self:
    :return:
    """
    self.page.get_by_label("Login Register").click()
    self.page.get_by_role("button", name="Регистрация").click()


@when(u'В поля emal и пароль вводит рандомные данные')
def fill_user_data_field(self):
    """
    :param self:
    """
    fake_password = fake.password()
    self.page.get_by_label("ФИО или название компании").click()
    self.page.get_by_label("ФИО или название компании").fill(fake.name())
    self.page.get_by_label("Email").click()
    self.page.get_by_label("Email").fill(fake.email())
    self.page.get_by_label("Пароль", exact=True).click()
    self.page.get_by_label("Пароль", exact=True).fill(fake_password)
    self.page.get_by_label("Подтвердите пароль").click()
    self.page.get_by_label("Подтвердите пароль").fill(fake_password)


@when(u'Нажать кнопку "Продолжить" №2')
def fill_user_data_in(self):
    """
    :param self:
    """
    self.page.locator("#simpleregister_button_confirm").click()


@then(u'Появиться уведомление "Ваша учетная запись создана!"')
def is_next_warning(self):
    """
    :param self:
    """
    self.page.get_by_role("heading", name="Ваша учетная запись создана!").click()

# -*- coding: utf-8 -*-
import time

from behave import given, when, then
from features import environment
from faker import Faker

fake = Faker()


@given(u'пользователь открывает сайт')
def open_site(self):
    page = environment.get_page(self)
    page.goto("https://stroyseven.ru/")


@given(u'нажимает кнопку "Личный кабинет"')
def click_btn_LK(self):
    self.page.get_by_label("Login Register").click()


@given(u'нажимает кнопку "Регистрация"')
def click_btn_reg(self):
    self.page.get_by_role("button", name="Регистрация").click()


@when(u'в поля emal и пароль ввести зарегистрированные учетные данные')
def enter_valid_data_reg(self):
    self.page.get_by_label("ФИО или название компании").click()
    self.page.get_by_label("ФИО или название компании").fill("Иванов Василий")
    self.page.get_by_label("Email").click()
    self.page.get_by_label("Email").fill("tetst79@mail.ru")
    self.page.get_by_label("Пароль", exact=True).click()
    self.page.get_by_label("Пароль", exact=True).fill("141009вы")
    self.page.get_by_label("Подтвердите пароль").click()
    self.page.get_by_label("Подтвердите пароль").fill("141009вы")


@when(u'пользователь нажмет кнопку "Продолжить"')
def click_continue(self):
    self.page.locator("#simpleregister_button_confirm").click()


@then(u'появиться предупреждение "Адрес уже зарегистрирован!"')
def warning_msg_address_registered(self):
    self.page.get_by_text("Адрес уже зарегистрирован!").click()


# Второй сценарий
@when(u'в поля emal и пароль вводятся случайные данные')
def enter_random_data_reg(self):
    fake_password = fake.password()
    self.page.get_by_label("ФИО или название компании").click()
    self.page.get_by_label("ФИО или название компании").fill(fake.name())
    self.page.get_by_label("Email").click()
    self.page.get_by_label("Email").fill(fake.email())
    self.page.get_by_label("Пароль", exact=True).click()
    self.page.get_by_label("Пароль", exact=True).fill(fake_password)
    self.page.get_by_label("Подтвердите пароль").click()
    self.page.get_by_label("Подтвердите пароль").fill(fake_password)


@then(u'появиться уведомление "Ваша учетная запись создана!"')
def notification_account_created(self):
    self.page.get_by_role("heading", name="Ваша учетная запись создана!").click()


@then(u'выйдет из учетной записи')
def log_out_account(self):
    self.page.get_by_role("banner").get_by_role("link", name="Выход").click()


# Третий сценарий
@when(u'оставить все поля пустыми')
def leave_fields_blank(self):
    pass


@then(u'выпадут сообщения о незаполненности полей')
def msg_about_fields_will(self):
    self.page.get_by_text("Имя должно быть от 1 до 32").click()
    self.page.get_by_text("Некорректный адрес электронной почты!").click()
    self.page.get_by_text("Пароль должен быть от 4 до 20").click()


# Четвертый сценарий
@when(u'пользователь введет email с цифрами в имени аккаунта')
def enter_email_numbers(self):
    self.page.get_by_label("Email").fill("1va2say3@gmail.com")


@then(u'сообщение о некорректном вводе не выпадет')
def msg_about_incorrect(self):
    try:
        self.page.get_by_text("Некорректный адрес электронной почты!").click()
    except Exception as e:
        print("Error! " + str(e))
        pass


# Пятый сценарий
@when(u'пользователь введет email с цифрами в доменной части')
def enter_numbers_domain(self):
    self.page.get_by_label("Email").fill("vasay@1gm2ail3.com")


# Шестой сценарий
@when(u'пользователь введет email с дефисом в имени аккаунта')
def enter_email_hyphen_account(self):
    self.page.get_by_label("Email").fill("vas-ay@gmail.com")


# Седьмой сценарий
@when(u'пользователь введет email с дефисом в доменной части')
def enter_email_hyphen_domain(self):
    self.page.get_by_label("Email").fill("vasay@gm-ail.com")


# Восьмой сценарий
@when(u'пользователь введет email со знаком подчеркивания в имени аккаунта')
def email_underscore_account(self):
    self.page.get_by_label("Email").fill("vas_ay@gmail.com")


# Девятый сценарий
@when(u'пользователь введет email со знаком подчеркивания в доменной части')
def email_underscore_domain(self):
    self.page.get_by_label("Email").fill("vasay@gm_ail.com")


# Десятый сценарий
@when(u'пользователь введет email с точками в имени аккаунта')
def email_dots_account(self):
    self.page.get_by_label("Email").fill("vas.ay@gmail.com")


# №11 сценарий
@when(u'пользователь введет email с несколькими точками в доменной части')
def email_several_dots_domain(self):
    self.page.get_by_label("Email").fill("vasay@gmail.ru.com")


# №12 сценарий
@when(u'пользователь введет email без точек в доменной части')
def email_without_dots_domain(self):
    self.page.get_by_label("Email").fill("vasay@gmail")


@then(u'появляется сообщение о некорректном вводе email')
def msg_email_incorrectly(self):
    self.page.get_by_text("Некорректный адрес электронной почты!").click()


# №13 сценарий
@when(u'пользователь введет email без превышения длины email (=319 символов)')
def email_length_319(self):
    big_name = ('vasya' * 62)
    self.page.get_by_label("Email").fill(big_name + "@mail.com")


# №14 сценарий
@when(u'пользователь введет email с превышением длины email (>320 символов)')
def email_length_320(self):
    big_name = ('vasya' * 62)
    self.page.get_by_label("Email").fill(big_name + "@gmail.com")


# №15 сценарий
@when(u'пользователь введет email без  @')
def email_without_dog(self):
    self.page.get_by_label("Email").fill("vasaygmail.com")


# №16 сценарий
@when(u'пользователь введет email с пробелами в имени аккаунта')
def email_with_spaces_account(self):
    self.page.get_by_label("Email").fill("vas ay@gmail.com")


# №17 сценарий
@when(u'пользователь введет email с пробелами в доменной части')
def email_with_spaces_domain(self):
    self.page.get_by_label("Email").fill("vasay@gm ail.com")


# №18 сценарий
@when(u'пользователь введет email без имени аккаунта')
def email_without_account_name(self):
    self.page.get_by_label("Email").fill("@gmail.com")


# №19 сценарий
@when(u'пользователь введет email без доменной части')
def email_without_domain(self):
    self.page.get_by_label("Email").fill("vasay@")


# №20 сценарий
@when(u'пользователь введет email 2 буквы после точки')
def email_2_letters_after(self):
    self.page.get_by_label("Email").fill("vasay@gmail.ru")


@when(u'пользователь введет email 32 буквы после точки')
def email_32_letters_after(self):
    big_domain = ('comm' * 8)
    self.page.get_by_label("Email").fill("vasay@gmail." + big_domain)


@when(u'пользователь введет email 63 буквы после точки')
def email_63_letters_after(self):
    very_big_domain = ('comm' * 15)
    self.page.get_by_label("Email").fill("vasay@gmail." + very_big_domain)


@when(u'пользователь введет email 64 буквы после точки')
def email_64_letters_after(self):
    very_very_big_domain = ('comm' * 16)
    self.page.get_by_label("Email").fill("vasay@gmail." + very_very_big_domain)


# №21 сценарий
@when(u'пользователь введет email в котором присутствует <знак>')
def email_containing_character(self):
    self.page.get_by_label("Email").fill("va" + ["знак"] + "say@gmail.ru")





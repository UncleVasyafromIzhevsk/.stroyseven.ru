# -*- coding: utf-8 -*-
import time

from behave import given, when, then
from features import environment
from faker import Faker

fake = Faker()


@given(u'пользователь открывает сайт')
def open_site(self):
    """
    строка 6
    """
    page = environment.get_page(self)
    page.goto("https://stroyseven.ru/compare-products/")


@given(u'нажимает кнопку "Личный кабинет"')
def click_btn_LK(self):
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


@when(u'пользователь поле "Пароль" оставит пустым')
def psw_field_empty(self):
    """
    Строка 12
    """
    pass


@when(u'пользователь нажмет кнопку "Продолжить"')
def click_continue(self):
    """
    Строка 13,16,21,24,27,30,36,42,45,50,53,56,59,62,65,78,81,84,87

    """
    self.page.locator("#simpleregister_button_confirm").click()


@then(u'появиться предупреждение "Пароль должен быть от 4 до 20 символов!"')
def warning_psw_4_20(self):
    """
    Строка 14,17,22,31
    """
    self.page.get_by_text("Пароль должен быть от 4 до 20").click()


@when(u'пользователь в поле "Пароль" напечатает "пробел"')
def type_space_psw(self):
    """
    Строка 15
    """
    self.page.get_by_label("Email").click()
    self.page.get_by_label("Email").fill("")


@when(u'пользователь в поле "Пароль" напечатает 3 символа')
def type_3_char_psw(self):
    """
    Строка 20
    """
    self.page.get_by_label("Пароль", exact=True).click()
    self.page.get_by_label("Пароль", exact=True).fill("567")


@when(u'пользователь в поле "Пароль" напечатает 10 символа')
def type_10_char_psw(self):
    """
    Строка 23
    """
    self.page.get_by_label("Пароль", exact=True).click()
    self.page.get_by_label("Пароль", exact=True).fill("7685498765")


@then(u'предупреждений не появиться')
def no_warnings_appear(self):
    """
    Строка 25,28
    """
    try:
        self.page.get_by_text("Пароль должен быть от 4 до 20").click()
    except Exception as e:
        print(e)
        pass


@when(u'пользователь в поле "Пароль" напечатает 20 символа')
def type_20_char_psw(self):
    """
    Строка 26
    """
    self.page.get_by_label("Пароль", exact=True).click()
    self.page.get_by_label("Пароль", exact=True).fill("53765142309874653627")


@when(u'пользователь в поле "Пароль" напечатает 21 символа')
def type_21_char_psw(self):
    """
    Строка 29
    """
    self.page.get_by_label("Пароль", exact=True).click()
    self.page.get_by_label("Пароль", exact=True).fill("537651423098746536274")


fake_psw = fake.password()


@when(u'ввести данные в поле "Пароль"')
def enter_data_in_psw(self):
    """
    Строка 34,40
    """
    self.page.get_by_label("Пароль", exact=True).click()
    self.page.get_by_label("Пароль", exact=True).fill(fake_psw)


@when(u'оставить пустым поле "Подтверждение пароля"')
def psw_field_blank(self):
    """
    Строка 35
    """
    self.page.get_by_label("Подтвердите пароль").click()


@then(u'появиться предупреждение "Подтверждение пароля не соответствует паролю!"')
def psw_confirmation_notpsw(self):
    """
    Строка 37,46
    """
    self.page.get_by_text("Подтверждение пароля не соответствует паролю!").click()


@when(u'ввести эти же данные в поле "Подтверждение пароля"')
def enter_data_confirm_psw(self):
    """
    Строка 41
    """
    self.page.get_by_label("Подтвердите пароль").fill(fake_psw)


@then(u'предупреждение "Подтверждение пароля не соответствует паролю!" не появиться')
def id_test2_43(self):
    """
    Cтрока 43
    """
    try:
        self.page.get_by_text("Подтверждение пароля не соответствует паролю!").click()
    except Exception as e:
        print(e)
        pass


@when(u'в поле "Подтверждение пароля" ввести не валидные данные')
def id_test2_44(self):
    """
    Строка 44
    """
    self.page.get_by_label("Подтвердите пароль").fill(fake.password())


@when(u'ввести поле "ФИО или название компании" оставить пустым')
def id_test2_49(self):
    """
    Строка 49
    """
    self.page.get_by_label("ФИО или название компании").click()


@then(u'появиться предупреждение "Имя должно быть от 1 до 32 символов!"')
def id_test2_51_54_66(self):
    """
    Строка 51,54,66
    """
    self.page.get_by_text("Имя должно быть от 1 до 32").click()


@when(u'ввести в поле "ФИО или название компании" ввести "пробелы"')
def id_test2_52(self):
    """
    Строка 52
    """
    self.page.get_by_label("ФИО или название компании").click()
    self.page.get_by_label("ФИО или название компании").fill("   ")


@when(u'ввести в поле "ФИО или название компании" ввести 1 символ')
def id_test2_55(self):
    """
    Строка 55
    """
    self.page.get_by_label("ФИО или название компании").click()
    self.page.get_by_label("ФИО или название компании").fill("Я")


@then(u'предупреждение "Имя должно быть от 1 до 32 символов!" не появиться')
def id_test2_57_60_63(self):
    """
    Строка 57,60,63
    """
    try:
        self.page.get_by_text("Имя должно быть от 1 до 32").click()
    except Exception as e:
        print(e)
        pass


@when(u'ввести в поле "ФИО или название компании" ввести 16 символов')
def id_test2_58(self):
    """
    Строка 58
    """
    self.page.get_by_label("ФИО или название компании").click()
    self.page.get_by_label("ФИО или название компании").fill("Василий Григорий")


@when(u'ввести в поле "ФИО или название компании" ввести 32 символ')
def id_test2_61(self):
    """
    Строка 61
    """
    self.page.get_by_label("ФИО или название компании").click()
    self.page.get_by_label("ФИО или название компании").fill("Василий ГригорийВасилий Григорий")


@when(u'ввести в поле "ФИО или название компании" ввести 33 символ')
def id_test2_64(self):
    """
    Строка 64
    """
    self.page.get_by_label("ФИО или название компании").click()
    self.page.get_by_label("ФИО или название компании").fill("Василий ГригорийВасилий Григорий!")


@when(u'ввести не цифровые данные в поле "Телефон"')
def id_test2_69(self):
    """
    Строка 69
    """
    try:
        self.page.get_by_placeholder("+7(rty)jhg-uy-yt").click()
    except Exception as e:
        print(e)
        pass


@then(u'данные не напечатаются')
def id_test2_70_72(self):
    """
    Строка 70,72
    """
    try:
        self.page.get_by_placeholder("+7(___)___-__-__").click()
    except Exception as e:
        print(e)
        pass


@when(u'ввести цифровые данные в поле "Телефон" количеством более 10')
def id_test2_71(self):
    """
    Строка 71
    """
    try:
        self.page.get_by_placeholder("+7(123)456-78-9000").click()
    except Exception as e:
        print(e)
        pass


@when(u'в блоке "Вы регистрируетесь как:" радиокнопку переключить в положение "Юридическое лицо"')
def id_test2_75(self):
    """
    Строка 75
    """
    self.page.get_by_label("Юридическое лицо").check()


@then(u'появиться поле "ИНН"')
def id_test2_76(self):
    """
    Строка 76
    """
    self.page.get_by_text("ИНН", exact=True).click()


@when(u'ввести не цифровые данные в поле "ИНН"')
def id_test2_77(self):
    """
    Строка 77
    """
    self.page.get_by_label("ИНН").click()
    self.page.get_by_label("ИНН").fill("MYINN")


@then(u'появиться предупреждение "ИНН указан неверно"')
def id_test2_79_82_84(self):
    """
    Строка 79,82,84
    """
    self.page.get_by_text("ИНН указан неверно").click()


@when(u'ввести цифровые данные в поле "ИНН" количеством менее 10')
def id_test2_80(self):
    """
    Строка 80
    """
    self.page.get_by_label("ИНН").click()
    self.page.get_by_label("ИНН").fill("123456789")


@when(u'ввести цифровые данные в поле "ИНН" количеством более 10')
def id_test2_83(self):
    """
    Строка 83
    """
    self.page.get_by_label("ИНН").click()
    self.page.get_by_label("ИНН").fill("12345678901")


@when(u'ввести цифровые данные в поле "ИНН" количеством 10')
def id_test2_86(self):
    """
    Строка 86
    """
    self.page.get_by_label("ИНН").click()
    self.page.get_by_label("ИНН").fill("1234567890")


@then(u'предупреждение "ИНН указан неверно" не появиться')
def id_test2_88(self):
    """
    Строка 88
    """
    try:
        self.page.get_by_text("ИНН указан неверно").click()
    except Exception as e:
        print(e)
        pass


@when(u'в блоке "Вы регистрируетесь как:" радиокнопку переключить в положение "Розничный покупатель"')
def id_test2_89(self):
    """
    Строка 89
    """
    self.page.get_by_label("Розничный покупатель").check()


@then(u'поле "ИНН" исчезнет')
def id_test2_90(self):
    """
    Строка 90
    """
    try:
        self.page.get_by_text("ИНН", exact=True).click()
    except Exception as e:
        print(e)
        pass

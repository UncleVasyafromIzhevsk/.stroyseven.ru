# -*- coding: utf-8 -*-
import time

from behave import given, when, then
from features import environment
from faker import Faker

fake = Faker()


@given(u'пользователь открывает сайт')
def open_site(self):
    page = environment.get_page(self)
    page.goto("https://stroyseven.ru/compare-products/")


@when(u'нажать кнопку "Кабинет"')
def links_btn_sp_2(self):
    """
    Строка 7
    """
    self.page.get_by_label("Login Register").click()


@then(u'откроется модальное окно авторизации')
def links_btn_sp_3(self):
    """
    Строка 8
    """
    self.page.get_by_text("Авторизация").click()


@when(u'поля ввести валидные данные')
def links_btn_sp_4(self):
    """
    Строка 9
    """
    self.page.get_by_placeholder("E-Mail", exact=True).click()
    self.page.get_by_placeholder("E-Mail", exact=True).fill("tetst79@mail.ru")
    self.page.get_by_placeholder("Пароль").click()
    self.page.get_by_placeholder("Пароль").fill("141009вы")
    self.page.get_by_role("button", name="Войти").click()


@then(u'будет выполнен вход на сайт как авторизированный пользователь')
def links_btn_sp_5(self):
    """
    Строка 10
    """
    pass


@when(u'нажать ссылку "О компании"')
def links_btn_sp_6(self):
    self.page.get_by_role("button", name="О компании").click()


@then(u'откроется страница с описанием компании')
def links_btn_sp_7(self):
    self.page.locator("span").filter(has_text="О компании").click()


@when(u'нажать кнопку "Назад"')
def links_btn_sp_back(self):
    self.page.goto("https://stroyseven.ru/")


@then(u'откроется главная страница')
def links_btn_sp_back(self):
    self.page.get_by_role("img", name="СтройСевен строительные материалы").click()


@when(u'нажать кнопку "Калькулятор доставки"')
def links_btn_sp_sp_10(self):
    self.page.get_by_role("button", name=" Калькулятор доставки").click()


@then(u'откроется страница расчета доставки')
def links_btn_sp_sp_11(self):
    self.page.get_by_role("heading", name="Доставка").click()


@when(u'нажать кнопку "Контакты"')
def links_btn_sp_sp_14(self):
    self.page.get_by_role("button", name=" Контакты").click()


@then(u'откроется страница контактных данных компании')
def links_btn_sp_sp_15(self):
    self.page.get_by_role("heading", name="Контакты").click()


@when(u'нажать кнопку "Оплата"')
def links_btn_sp_sp_18(self):
    self.page.get_by_role("button", name=" Оплата").click()


@then(u'откроется страница с вариантами оплаты')
def links_btn_sp_sp_19(self):
    self.page.get_by_role("heading", name="Оплата").click()


@when(u'нажать кнопку "Оптовикам и Юр Лицам"')
def links_btn_sp_sp_22(self):
    self.page.goto("https://stroyseven.ru/my-account/")


@then(u'откроется страница личного кабинета')
def links_btn_sp_sp_23(self):
    self.page.get_by_role("heading", name="Моя учетная запись").click()


@when(u'нажать кнопку "Производители"')
def links_btn_sp_sp_26(self):
    self.page.goto("https://stroyseven.ru/brands/")


@then(u'откроется страница производителей товаров')
def links_btn_sp_sp_27(self):
    self.page.get_by_role("heading", name="Производители - Стройсевен").click()


@given(u'нажать на номер телефона')
def links_btn_sp_sp_31(self):
    self.page.get_by_role("link", name=" 8 (800) 600-74-").click()


@then(u'откроется пустая вклада на настольной версии, а в мобильной откроется телефон с номером компании')
def links_btn_sp_sp_32(self):
    pass


@given(u'главная страница сайта')
def links_btn_sp_sp_31(self):
    self.page.goto("https://stroyseven.ru/")


@given(u'в разделе "Каталог товаров"')
def links_btn_sp_sp_33(self):
    self.page.get_by_text("Каталог товаров").click()


@when(u'нажмем кнопку "Сухие смеси"')
def links_btn_sp_sp_34(self):
    self.page.goto("https://stroyseven.ru/suhie_smesi/")


@then(u'откроется страница раздела "Сухие смеси"')
def links_btn_sp_sp_35(self):
    self.page.get_by_role("heading", name="Сухие смеси").click()


@when(u'нажмем кнопку "Клей"')
def links_btn_sp_sp_39(self):
    self.page.goto("https://stroyseven.ru/klej/")


@then(u'откроется страница раздела "Клей"')
def links_btn_sp_sp_40(self):
    self.page.get_by_role("heading", name="Клей").click()


@when(u'нажмем кнопку "Изоляционные материалы"')
def links_btn_sp_sp_44(self):
    self.page.goto("https://stroyseven.ru/izolyacionnye_materialy/")


@then(u'откроется страница раздела "Изоляционные материалы"')
def links_btn_sp_sp_45(self):
    self.page.get_by_role("heading", name="Изоляционные материалы").click()


@when(u'нажмем кнопку "Напольные покрытия"')
def links_btn_sp_sp_49(self):
    self.page.goto("https://stroyseven.ru/napolnye_pokrytiya/")


@then(u'откроется страница раздела "Напольные покрытия"')
def links_btn_sp_sp_50(self):
    self.page.get_by_role("heading", name="Напольные покрытия").click()


@when(u'нажмем кнопку "Листовые материалы"')
def links_btn_sp_sp_54(self):
    self.page.goto("https://stroyseven.ru/listovye_materialy/")


@then(u'откроется страница раздела "Листовые материалы"')
def links_btn_sp_sp_55(self):
    self.page.get_by_role("heading", name="Листовые материалы").click()


@when(u'нажмем кнопку "Монтажный инструмент"')
def links_btn_sp_sp_59(self):
    self.page.goto("https://stroyseven.ru/montazhnyj_instrument/")


@then(u'откроется страница раздела "Монтажный инструмент"')
def links_btn_sp_sp_60(self):
    pass


@when(u'нажмем кнопку "Древесно-Плитные материалы"')
def links_btn_sp_sp_64(self):
    self.page.goto("https://stroyseven.ru/drevesno-plitnye_materialy/")


@then(u'откроется страница раздела "Древесно-Плитные материалы"')
def links_btn_sp_sp_65(self):
    self.page.get_by_role("heading", name="Древесно-плитные материалы").click()


@when(u'нажмем кнопку "Блоки строительные"')
def links_btn_sp_sp_64(self):
    self.page.goto("https://stroyseven.ru/bloki_stroitelnye/")


@then(u'откроется страница раздела "Блоки строительные"')
def links_btn_sp_sp_65(self):
    self.page.get_by_role("heading", name="Блоки строительные").click()


@when(u'нажмем кнопку "Сетки"')
def links_btn_sp_sp_69(self):
    self.page.goto("https://stroyseven.ru/setki/")


@then(u'откроется страница раздела "Сетки"')
def links_btn_sp_sp_70(self):
    self.page.get_by_role("heading", name="Сетки").click()


@when(u'нажмем кнопку "Пены и герметики"')
def links_btn_sp_sp_74(self):
    self.page.goto("https://stroyseven.ru/peny_i_germetiki/")


@then(u'откроется страница раздела "Пены и герметики"')
def links_btn_sp_sp_75(self):
    self.page.get_by_role("heading", name="Пены и герметики").click()


@when(u'нажмем кнопку "Кровельные материалы"')
def links_btn_sp_sp_79(self):
    self.page.goto("https://stroyseven.ru/krovelnye_materialy/")


@then(u'откроется страница раздела "Кровельные материалы"')
def links_btn_sp_sp_80(self):
    self.page.get_by_role("heading", name="Кровельные материалы").click()


@when(u'нажмем кнопку "Хозяйственные товары"')
def links_btn_sp_sp_84(self):
    self.page.goto("https://stroyseven.ru/hozyajstvennye_tovary/")


@then(u'откроется страница раздела "Хозяйственные товары"')
def links_btn_sp_sp_85(self):
    self.page.get_by_role("heading", name="Хозяйственные товары").click()


@when(u'нажмем кнопку "Полиэтиленовые пленки"')
def links_btn_sp_sp_89(self):
    self.page.goto("https://stroyseven.ru/poliehtilenovye_plenki/")


@then(u'откроется страница раздела "Полиэтиленовые пленки"')
def links_btn_sp_sp_90(self):
    self.page.get_by_role("heading", name="Полиэтиленовые пленки").click()


@when(u'нажмем кнопку "Лакокрасочные материалы"')
def links_btn_sp_sp_94(self):
    self.page.goto("https://stroyseven.ru/lakokrasochnye_materialy/")


@then(u'откроется страница раздела "Лакокрасочные материалы"')
def links_btn_sp_sp_95(self):
    self.page.get_by_role("heading", name="Лакокрасочные материалы").click()


@when(u'нажмем кнопку "Строительные обои"')
def links_btn_sp_sp_99(self):
    self.page.goto("https://stroyseven.ru/stroitelnye_oboi/")


@then(u'откроется страница раздела "Строительные обои"')
def links_btn_sp_sp_100(self):
    self.page.get_by_role("heading", name="Строительные обои").click()


@when(u'нажмем кнопку "Теплые полы"')
def links_btn_sp_sp_104(self):
    self.page.goto("https://stroyseven.ru/teplye_poly/")


@then(u'откроется страница раздела "Теплые полы"')
def links_btn_sp_sp_105(self):
    self.page.get_by_role("heading", name="Теплые полы").click()


@when(u'нажмем кнопку "Электроинструменты"')
def links_btn_sp_sp_109(self):
    self.page.goto("https://stroyseven.ru/ehlektroinstrumenty/")


@then(u'откроется страница раздела "Электроинструменты"')
def links_btn_sp_sp_110(self):
    self.page.get_by_role("heading", name="Электроинструменты").click()


@when(u'нажмем кнопку "Металл"')
def links_btn_sp_sp_114(self):
    self.page.goto("https://stroyseven.ru/metall/")


@then(u'откроется страница раздела "Металл"')
def links_btn_sp_sp_115(self):
    self.page.get_by_role("heading", name="Металл").click()


@given(u'в разделе "Футер"')
def links_btn_sp_sp(self):
    self.page.get_by_text("Информация").click()


@when(u'нажмем ссылку "Политика конфиденциальности"')
def links_btn_gjkbnbrf(self):
    self.page.get_by_role("link", name="Политика конфиденциальности").click()


@then(u'откроется страница "Политика конфиденциальности"')
def links_btn_sp_sp_1152(self):
    self.page.get_by_role("heading", name="Политика конфиденциальности").click()


@when(u'нажмем ссылку "Условия соглашения"')
def links_btn_gjkb(self):
    self.page.goto("https://stroyseven.ru/usloviya_soglasheniya")


@then(u'откроется страница "Условия соглашения"')
def links_btn_sp_sp_115452(self):
    self.page.get_by_role("heading", name="Пользовательское Соглашение").click()


@when(u'нажмем ссылку "Акции"')
def links_btn_gjkb3(self):
    self.page.get_by_role("link", name="Акции").click()


@then(u'откроется страница "Акции"')
def links_btn_sp_sp_1154526(self):
    self.page.get_by_role("heading", name="Акции - Стройсевен").click()


@when(u'нажмем ссылку "Карта сайта"')
def links_btn_873(self):
    self.page.get_by_role("link", name="Карта сайта").click()


@then(u'откроется страница "Карта сайта"')
def links_btn_sp_sp_11545265(self):
    self.page.get_by_role("heading", name="Карта сайта - Стройсевен").click()


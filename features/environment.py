from datetime import datetime
import logging
from playwright.sync_api import sync_playwright


def before_all(context):
    """
    Метод для создания экземпляра страницы перед всеми сценариями
    @Author: Чирков Сергей
    @Date: 28.05.2024
    :param context:
    :return:
    """
    global _page
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False, slow_mo=1000, channel="chrome")
    context.page = browser.new_page()
    _page = context.page
    set_page(context, _page)


def get_page(self):
    """
    Метод получения экземпляра страницы
    @Author: Чирков Сергей
    @Date: 28.05.2024
    :param self:
    :return:
    """
    return self._page


def set_page(self, _page):
    """
    Метод установки экземпляра страницы
    @Author: Чирков Сергей
    @Date: 28.05.2024
    :param self:
    :param _page:
    :return:
    """
    self._page = _page


def after_all(context):
    """
    Метод закроет все сеансы браузера после выполнения всех файлов функций.
    @Author: Чирков Сергей
    @Date: 28.05.2024
    :param context:
    :return:
    """
    _page.close()
    print("\nAfter all Feature")


def before_feature(context, feature):
    """
    Метод будет выполняться перед каждой функцией
    @Author: Чирков Сергей
    @Date: 28.05.2024
    :param context:
    :param feature:
    :return:
    """
    # Create logger
    context.logger = logging.getLogger('automation_tests')
    context.logger.setLevel(logging.DEBUG)


def after_feature(context, feature):
    """
    Метод будет выполняться после каждой функции
    @Author: Чирков Сергей
    @Date: 28.05.2024
    :param context:
    :param feature:
    :return:
    """
    #print("\nAfter Feature")


def before_scenario(context, scenario):
    """
    Метод будет выполняться перед каждым сценарием
    @Author: Чирков Сергей
    @Date: 28.05.2024
    :param context:
    :param scenario:
    :return:
    """
    #print("Before scenario\n")


def after_scenario(context, scenario):
    """
    Метод будет выполняться после каждого сценария
    @Author: Чирков Сергей
    @Date: 28.05.2024
    :param context:
    :param scenario:
    :return:
    """
    if scenario.status == 'failed':
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        screenshot_path = f'failure_screenshots/{scenario.name}_{timestamp}.png'
        context.page.screenshot(path=screenshot_path)
    #print("After scenario\n")


def before_step(context, step):
    """
    Метод будет выполняться перед каждым шагом
    @Author: Чирков Сергей
    @Date: 28.05.2024
    :param context:
    :param step:
    :return:
    """
    #print("After step\n")


def after_step(context, step):
    """
    Метод будет выполняться после каждого шага
    @Author: Чирков Сергей
    @Date: 28.05.2024
    :param context:
    :param step:
    :return:
    """
    #print("After step\n")
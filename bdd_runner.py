import os
import subprocess
from datetime import datetime


def execute_features():
    """
    Метод помогает запускать файлы функций и генерировать отчет BDD.
    @Author: Чирков Сергей
    @Date: 28.05.2024
    :return:
    """
    current_directory = os.getcwd()
    new_folder_path = os.path.join(current_directory, 'отчеты_по_тестам')
    if not os.path.exists(new_folder_path):
        os.mkdir(new_folder_path)
    htmlpath = 'отчеты_по_тестам' + '\\' + 'Отчет_автоматизированного_тестирования' \
               + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"

    command = ["behave", "-f", "html-pretty", "-o", htmlpath]

    subprocess.run(command, check=True)
    print("Тестовые выполнены успешно. Отчет будет доступен по адресу " + htmlpath)


if __name__ == '__main__':
    execute_features()
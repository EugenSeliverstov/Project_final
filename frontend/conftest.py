import time
import pytest
from selenium import webdriver
from home_page import HomePage
from login_page import LoginPage

@pytest.fixture(scope="class")
def init_driver(request):

    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(options=options)

    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver

    # Инициализация страниц
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    # Открытие страницы авторизации
    login_page.open_login_page()

    # Авторизация
    login_page.login_user()
    time.sleep(10)

    # Вход на сервер "Диплом"
    home_page.clic_to_server_diploma()
    time.sleep(10)

    # Переход в канал "6"
    home_page.clic_to_channel()
    time.sleep(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def base_url():
    return 'https://discord.com/login'






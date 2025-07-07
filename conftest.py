import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import MAIN_URL, TEST_EMAIL, TEST_PASSWORD, REGISTER_URL
from locators import LoginPageLocators
from pages.regis_page import RegisterPage
from pages.login_page import LoginPage
from generator_log_pas import generate_email, generate_password

@pytest.fixture
def driver():
    """
    Фикстура для инициализации драйвера браузера.
    Открывает браузер перед тестом и закрывает после выполнения.
    
    Returns:
        WebDriver: экземпляр браузера
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def login_user(driver):
    """
    Логинит пользователя и возвращает страницу после авторизации.
    Args:
        driver (WebDriver): экземпляр браузера
    Returns:
        LoginPage: экземпляр страницы после входа
    """
    driver.get(MAIN_URL)
    page = LoginPage(driver)
    page.click_enter_account()
    page.set_email(TEST_EMAIL)
    page.set_password(TEST_PASSWORD)
    page.click_login()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.CREATE_ORDER_BUTTON)
    )
    return page

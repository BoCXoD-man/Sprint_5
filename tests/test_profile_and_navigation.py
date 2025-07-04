import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import MAIN_URL
from locators import HeaderLocators, LoginPageLocators
import time


def test_go_to_profile(login_user):
    """
    Тестирует переход в личный кабинет после входа.
    Args:
        login_user (LoginPage): залогиненная страница
    """
    login_user.click(HeaderLocators.PERSONAL_ACCOUNT_BUTTON)
    WebDriverWait(login_user.driver, 5).until(
        EC.url_contains("/account/profile")
    )
    assert "/account/profile" in login_user.get_current_url()
    assert login_user.is_visible(LoginPageLocators.SAVE_BUTTON) == True, "Кнопка 'Сохранить' не видна"


def test_go_from_profile_to_constructor_button(login_user):
    """
    Тестирует переход из профиля в конструктор по кнопке "Конструктор".
    Args:
        login_user (LoginPage): залогиненная страница
    """
    login_user.click(HeaderLocators.PERSONAL_ACCOUNT_BUTTON)
    login_user.click(HeaderLocators.CONSTRUCTOR_BUTTON)
    WebDriverWait(login_user.driver, 5).until(
        EC.url_matches(MAIN_URL + "/")
    )
    assert login_user.get_current_url() == MAIN_URL + "/", "Не произошел переход на главную страницу"
    assert login_user.is_visible(HeaderLocators.CONSTRUCTOR_BUTTON) == True, "Кнопка 'Конструктор' не видна"


def test_go_from_profile_to_constructor_logo(login_user):
    """
    Тестирует переход в конструктор по клику на логотип Stellar Burgers.
    Args:
        login_user (LoginPage): залогиненная страница
    """
    login_user.click(HeaderLocators.PERSONAL_ACCOUNT_BUTTON)
    login_user.click(HeaderLocators.STELLAR_LOGO)
    WebDriverWait(login_user.driver, 5).until(
        EC.url_matches(MAIN_URL + "/")
    )
    assert login_user.get_current_url() == MAIN_URL + "/", "Не произошел переход на главную страницу"
    assert login_user.is_visible(HeaderLocators.CONSTRUCTOR_BUTTON) == True, "Кнопка 'Конструктор' не видна"

def test_logout_from_profile(login_user):
    """
    Тестирует выход из аккаунта через личный кабинет.
    Args:
        login_user(LoginPage): залогиненная страница
    """
    login_user.click(HeaderLocators.PERSONAL_ACCOUNT_BUTTON)
    login_user.click(HeaderLocators.LOGOUT_BUTTON)
    WebDriverWait(login_user.driver, 5).until(
        EC.url_contains("/login")
    )
    assert "/login" in login_user.get_current_url()
    assert login_user.is_visible(LoginPageLocators.LOGIN_BUTTON) == True, "Кнопка 'Войти в аккаунт' не видна"


def test_switch_constructor_tabs(login_user):
    """
    Тестирует переключение между вкладками конструктора: Булки, Соусы, Начинки.
    Args:
        login_user (LoginPage): залогиненная страница
    """
    login_user.click(HeaderLocators.CONSTRUCTOR_BUTTON)

    # Соусы
    login_user.click(HeaderLocators.SAUCE_TAB)
    WebDriverWait(login_user.driver, 5).until(
        EC.text_to_be_present_in_element(HeaderLocators.ACTIVE_TAB, "Соусы"))
    
    time.sleep(0.5) # Задержка для стабильности теста
    # Без нее(задержки в 0.5 сек) часто неуспевает обновиться текст активной вкладки  и тест заваливается
    assert "Соусы" in login_user.get_text(HeaderLocators.ACTIVE_TAB)

    # Начинки
    login_user.click(HeaderLocators.FILLING_TAB)
    WebDriverWait(login_user.driver, 5).until(
        EC.text_to_be_present_in_element(HeaderLocators.ACTIVE_TAB, "Начинки")
    )
    time.sleep(0.5) # Задержка для стабильности теста
    assert "Начинки" in login_user.get_text(HeaderLocators.ACTIVE_TAB)

    # Булки
    login_user.click(HeaderLocators.BUN_TAB)
    WebDriverWait(login_user.driver, 5).until(
        EC.text_to_be_present_in_element(HeaderLocators.ACTIVE_TAB, "Булки"))
    time.sleep(0.5)  # Задержка для стабильности теста
    assert "Булки" in login_user.get_text(HeaderLocators.ACTIVE_TAB)
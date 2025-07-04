from pages.login_page import LoginPage
from constants import MAIN_URL, REGISTER_URL, TEST_EMAIL, TEST_PASSWORD
from locators import LoginPageLocators
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("email,password", [(TEST_EMAIL, TEST_PASSWORD)])
def test_login_from_main_page(driver, email, password):
    """ Вход по кнопке "Войти в аккаунт" на главной"""
    driver.get(MAIN_URL)
    page = LoginPage(driver)

    page.click_enter_account()  # Клик по кнопке "Войти в аккаунт"
    page.login(email, password) # Авторизация

    # Ожидание появления кнопки "Оформить заказ"
    WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located(LoginPageLocators.CREATE_ORDER_BUTTON))

    # Первый вариант, как убедиться, что авторизация прошла успешно
    # Проверка успешного входа: Видна кнопка "Оформить заказ" и на нужной странице
    assert page.is_visible(LoginPageLocators.CREATE_ORDER_BUTTON) == True, "Кнопка 'Оформить заказ' не видна"
    assert '/login' not in page.get_current_url(), "Не на главной странице после входа"

    

@pytest.mark.parametrize("email,password", [(TEST_EMAIL, TEST_PASSWORD)])
def test_login_from_profile_button(driver, email, password):
    """ Вход через кнопку «Личный кабинет»"""
    driver.get(MAIN_URL)
    page = LoginPage(driver)

    page.click_personal_account()  # Клик по кнопке "Личный Кабинет"
    page.login(email, password)    # Авторизация

    # Ожидание появления кнопки "Оформить заказ"
    WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located(LoginPageLocators.CREATE_ORDER_BUTTON))

    # Второй вариант, как убедиться, что авторизация прошла успешно
    # Переход в личный кабинет и убедиться, что кнопка "Сохранить" видна и мы на нужной странице
    page.click_personal_account()
    time.sleep(1)

    # Проверка успешного входа
    assert "/account/profile" in page.get_current_url(), "Не произошел переход в личный кабинет"
    assert page.is_visible(LoginPageLocators.SAVE_BUTTON) == True, "Кнопка 'Сохранить' не видна"


@pytest.mark.parametrize("email,password", [(TEST_EMAIL, TEST_PASSWORD)])
def test_login_from_register_form(driver, email, password):
    """ Вход через кнопку в форме регистрации"""
    driver.get(REGISTER_URL)
    page = LoginPage(driver)

    page.click(LoginPageLocators.ENTER_REGISTRATION_BUTTON) # Клик по кнопке "Войти" в форме регистрации
    page.login(email, password)  # Авторизация

    # Ожидание появления кнопки "Оформить заказ"
    WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located(LoginPageLocators.CREATE_ORDER_BUTTON))
    
    # Второй вариант, как убедиться, что авторизация прошла успешно
    # Переход в личный кабинет и убедиться, что кнопка "Сохранить" видна и мы на нужной странице
    page.click_personal_account()
    time.sleep(0.5)

    # Проверка успешного входа
    assert "/account/profile" in page.get_current_url(), "Не произошел переход в личный кабинет"
    assert page.is_visible(LoginPageLocators.SAVE_BUTTON) == True, "Кнопка 'Сохранить' не видна"


@pytest.mark.parametrize("email,password", [(TEST_EMAIL, TEST_PASSWORD)])
def test_login_from_forgot_password_form(driver, email, password):
    """ Вход через кнопку в форме восстановления пароля"""
    driver.get(f"{MAIN_URL}/forgot-password")

    page = LoginPage(driver)

    page.click((By.XPATH, "//a[text() = 'Войти']")) # Клик по кнопке "Войти" в форме восстановления пароля
    page.login(email, password) # Авторизация

    WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located(LoginPageLocators.CREATE_ORDER_BUTTON))
    page.click_personal_account()
    time.sleep(0.5)

    # Проверка успешного входа
    assert "/account/profile" in page.get_current_url(), "Не произошел переход в личный кабинет"
    assert page.is_visible(LoginPageLocators.SAVE_BUTTON) == True, "Кнопка 'Сохранить' не видна"

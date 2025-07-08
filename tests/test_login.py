from pages.login_page import LoginPage
from constants import MAIN_URL, REGISTER_URL, TEST_EMAIL, TEST_PASSWORD
from locators import LoginPageLocators
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestLoginScenarios:
    """Тесты различных сценариев входа в систему"""
    
    @pytest.mark.parametrize("email,password", [(TEST_EMAIL, TEST_PASSWORD)])
    def test_login_from_main_page(self, driver, email, password):
        """Тест входа по кнопке 'Войти в аккаунт' на главной"""
        driver.get(MAIN_URL)
        page = LoginPage(driver)

        page.click_enter_account()
        page.login(email, password)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.CREATE_ORDER_BUTTON))

        assert page.is_visible(LoginPageLocators.CREATE_ORDER_BUTTON), "Кнопка 'Оформить заказ' не видна"
        assert '/login' not in page.get_current_url(), "Не на главной странице после входа"

    @pytest.mark.parametrize("email,password", [(TEST_EMAIL, TEST_PASSWORD)])
    def test_login_from_profile_button(self, driver, email, password):
        """Тест входа через кнопку 'Личный кабинет'"""
        driver.get(MAIN_URL)
        page = LoginPage(driver)

        page.click_personal_account()
        page.login(email, password)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.CREATE_ORDER_BUTTON))

        page.click_personal_account()
        WebDriverWait(driver, 5).until(
            EC.url_contains("/account/profile"))

        assert "/account/profile" in page.get_current_url(), "Не произошел переход в личный кабинет"
        assert page.is_visible(LoginPageLocators.SAVE_BUTTON), "Кнопка 'Сохранить' не видна"

    @pytest.mark.parametrize("email,password", [(TEST_EMAIL, TEST_PASSWORD)])
    def test_login_from_register_form(self, driver, email, password):
        """Тест входа через кнопку в форме регистрации"""
        driver.get(REGISTER_URL)
        page = LoginPage(driver)

        page.click(LoginPageLocators.ENTER_REGISTRATION_BUTTON)
        page.login(email, password)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.CREATE_ORDER_BUTTON))
        
        page.click_personal_account()
        WebDriverWait(driver, 5).until(
            EC.url_contains("/account/profile"))

        assert "/account/profile" in page.get_current_url(), "Не произошел переход в личный кабинет"
        assert page.is_visible(LoginPageLocators.SAVE_BUTTON), "Кнопка 'Сохранить' не видна"

    @pytest.mark.parametrize("email,password", [(TEST_EMAIL, TEST_PASSWORD)])
    def test_login_from_forgot_password_form(self, driver, email, password):
        """Тест входа через кнопку в форме восстановления пароля"""
        driver.get(f"{MAIN_URL}/forgot-password")
        page = LoginPage(driver)

        page.click((By.XPATH, "//a[text() = 'Войти']"))
        page.login(email, password)

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.CREATE_ORDER_BUTTON))

        page.click_personal_account()
        WebDriverWait(driver, 5).until(
            EC.url_contains("/account/profile"))

        assert "/account/profile" in page.get_current_url(), "Не произошел переход в личный кабинет"
        assert page.is_visible(LoginPageLocators.SAVE_BUTTON), "Кнопка 'Сохранить' не видна"

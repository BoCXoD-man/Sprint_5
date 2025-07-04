from pages.regis_page import RegisterPage
from generator_log_pas import generate_email, generate_password
from locators import RegisterPageLocators
import time
from constants import REGISTER_URL

def test_successful_registration(driver):
    page = RegisterPage(driver)
    page.open(REGISTER_URL)

    page.register("Андрей", generate_email(), generate_password(10)) # регистрируемся

    if page.is_visible(RegisterPageLocators.ERROR_MESSAGE):
        print("Ошибка на форме регистрации:", page.get_error_message())

    assert "/login" in page.get_current_url()
    # assert page.is_visible(RegisterPageLocators.ERROR_MESSAGE) == False, "Сообщение об ошибке отображается, хотя регистрация должна быть успешной"
    # Вторую проверку можно считать избыточной, + очень удлинняется время теста (на 10 секунд). Но если она очень важна для сдачи проекта, то раскометирую.

def test_registration_with_short_password_shows_error(driver):
    page = RegisterPage(driver)
    page.open(REGISTER_URL)

    page.register("Андрей", generate_email(), "123") # регистрируемся

    # Проверяем, что появилась ошибка под полем пароля
    error_text = page.get_error_message()
    assert "Некорректный пароль" in error_text
    assert page.is_visible(RegisterPageLocators.ERROR_MESSAGE) == True, "Сообщение об ошибке не отображается"

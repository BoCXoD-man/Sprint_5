from pages.regis_page import RegisterPage
from generator_log_pas import generate_email, generate_password
from locators import RegisterPageLocators
from constants import REGISTER_URL


class TestRegistrationScenarios:
    """Тесты различных сценариев регистрации"""
    
    def test_successful_registration(self, driver):
        """Тест успешной регистрации нового пользователя"""
        page = RegisterPage(driver)
        page.open(REGISTER_URL)

        page.register("Андрей", generate_email(), generate_password(10))

        if page.is_visible(RegisterPageLocators.ERROR_MESSAGE):
            print("Ошибка на форме регистрации:", page.get_error_message())

        assert "/login" in page.get_current_url(), "Не произошел переход на страницу входа после регистрации"

    def test_registration_with_short_password_shows_error(self, driver):
        """Тест регистрации с коротким паролем (валидация ошибки)"""
        page = RegisterPage(driver)
        page.open(REGISTER_URL)

        page.register("Андрей", generate_email(), "123")

        error_text = page.get_error_message()
        assert "Некорректный пароль" in error_text, "Неверное сообщение об ошибке"
        assert page.is_visible(RegisterPageLocators.ERROR_MESSAGE), "Сообщение об ошибке не отображается"
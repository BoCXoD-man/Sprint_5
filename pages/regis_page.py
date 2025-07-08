from locators import RegisterPageLocators
from pages.base_page import BasePage

class RegisterPage(BasePage):
    def set_name(self, name):
        """ Вводит текст(имя) в поле ввода
        Args:
            name (str): имя"""
        self.type(RegisterPageLocators.NAME_INPUT, name)

    def set_email(self, email):
        """ Вводит текст(почту) в поле ввода
        Args:
            email (str): почта"""
        self.type(RegisterPageLocators.EMAIL_INPUT, email)

    def set_password(self, password):
        """ Вводит текст(пароль) в поле ввода
        Args:
            password (str): пароль"""
        self.type(RegisterPageLocators.PASSWORD_INPUT, password)

    def click_register(self):
        """Кликает по кнопке регистрации"""
        self.click(RegisterPageLocators.REGISTER_BUTTON)

    def register(self, name: str, email: str, password: str):
        """Полностью выполняет регистрацию.
        Args:
            name (str): имя
            email (str): почта
            password (str): пароль
        """
        self.set_name(name)
        self.set_email(email)
        self.set_password(password)
        self.click_register()

    def get_error_message(self):
        """Возвращает текст ошибки"""
        return self.get_text(RegisterPageLocators.ERROR_MESSAGE)

from locators import LoginPageLocators
from pages.base_page import BasePage

class LoginPage(BasePage):

    def set_email(self, email):
        """Вводит email в поле ввода
        Args:
            email (str): email для ввода
        """
        self.type(LoginPageLocators.EMAIL_INPUT, email)

    def set_password(self, password):
        """Вводит пароль в поле ввода
        Args:
            password (str): пароль для ввода
        """
        self.type(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login(self):
        """Кликает по кнопке входа"""
        self.click(LoginPageLocators.LOGIN_BUTTON)
    
    def click_enter_account(self):
        """Кликает по кнопке "Войти в аккаунт" на главной странице"""
        self.click(LoginPageLocators.ENTER_ACCOUNT_BUTTON)

    def click_personal_account(self):
        """Кликает по кнопке "Личный Кабинет" на главной странице"""
        self.click(LoginPageLocators.PERSONAL_ACCOUNT_BUTTON)
        
    def get_error_message(self):
        """Возвращает текст ошибки
        Returns:
            str: текст ошибки
        """
        return self.get_text(LoginPageLocators.ERROR_MESSAGE)
    
    def login(self, email: str, password: str):
        """Полностью выполняет авторизацию.
        Args:
            email (str): логин
            password (str): пароль
        """
        self.set_email(email)
        self.set_password(password)
        self.click_login()

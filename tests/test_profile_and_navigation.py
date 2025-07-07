from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import MAIN_URL
from locators import HeaderLocators, LoginPageLocators


class TestProfileNavigation:
    """Тесты навигации: личный кабинет и конструктор"""
    
    def test_go_to_profile(self, login_user):
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
        assert login_user.is_visible(LoginPageLocators.SAVE_BUTTON), "Кнопка 'Сохранить' не видна"

    def test_go_from_profile_to_constructor_button(self, login_user):
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
        assert login_user.is_visible(HeaderLocators.CONSTRUCTOR_BUTTON), "Кнопка 'Конструктор' не видна"

    def test_go_from_profile_to_constructor_logo(self, login_user):
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
        assert login_user.is_visible(HeaderLocators.CONSTRUCTOR_BUTTON), "Кнопка 'Конструктор' не видна"

    def test_logout_from_profile(self, login_user):
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
        assert login_user.is_visible(LoginPageLocators.LOGIN_BUTTON), "Кнопка 'Войти в аккаунт' не видна"


class TestConstructorTabs:
    """Тесты переключения вкладок конструктора"""
    
    def test_switch_constructor_tabs(self, login_user):
        """
        Тестирует переключение между вкладками конструктора: Булки, Соусы, Начинки.
        Args:
            login_user (LoginPage): залогиненная страница
        """
        login_user.click(HeaderLocators.CONSTRUCTOR_BUTTON)
        
        login_user.switch_and_verify_tab(HeaderLocators.SAUCE_TAB, "Соусы")
        login_user.switch_and_verify_tab(HeaderLocators.FILLING_TAB, "Начинки")
        login_user.switch_and_verify_tab(HeaderLocators.BUN_TAB, "Булки")
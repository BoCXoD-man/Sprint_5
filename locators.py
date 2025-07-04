from selenium.webdriver.common.by import By


class RegisterPageLocators:
    """Локаторы для страницы регистрации"""
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле для ввода имени
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input") # Поле для ввода email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле для ввода пароля
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    ERROR_MESSAGE = (By.CLASS_NAME, "input__error")  # Сообщение об ошибке для некорректного пароля


class LoginPageLocators:
    """Локаторы для страницы логина"""
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле для ввода email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле для ввода пароля
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"
    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Личный Кабинет" на главной странице
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//nav/a/p[text()='Личный Кабинет']")  # Кнопка "Личный Кабинет"
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ" на странице
    ERROR_MESSAGE = (By.CLASS_NAME, "input__error")  # Сообщение об ошибке
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")  # Кнопка "Сохранить" в личном кабинете
    ENTER_REGISTRATION_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj")  # Кнопка "Войти" в форме регистрации


class HeaderLocators:
    """Локаторы для элементов шапки сайта"""
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']") # Кнопка "Личный Кабинет" в шапке
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") # Кнопка "Конструктор" в шапке
    STELLAR_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # Логотип Stellar Burgers в шапке
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") # Кнопка "Выход" в личном кабинете

    # Разделы конструктора
    BUN_TAB = (By.XPATH, "//span[text()='Булки']") # Вкладка "Булки"
    SAUCE_TAB = (By.XPATH, "//span[text()='Соусы']") # Вкладка "Соусы"
    FILLING_TAB = (By.XPATH, "//span[text()='Начинки']") # Вкладка "Начинки"
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]") # Активная вкладка конструктора

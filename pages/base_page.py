from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import HeaderLocators
from selenium.common.exceptions import TimeoutException

class BasePage:
    """
    Базовый класс для всех страниц.
    Содержит общие методы: клик, ввод текста, получение текста и т.д.
    """

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        """
        Открывает заданный URL
        Args:
            url (str): URL
        """
        self.driver.get(url)

    def find(self, locator):
        """Находит и возвращает видимый элемент
        Args:
            locator (tuple): кортеж с локатором
        Returns:
            WebElement: видимый элемент"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        """Возвращает список всех найденных элементов
        Args:
            locator (tuple): кортеж с локатором
        Returns:
            list: список элементов"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        """Кликает по найденному элементу
        Args:
            locator (tuple): кортеж с локатором"""
        self.find(locator).click()

    def type(self, locator, text):
        """
        Вводит текст в поле ввода
        Означает: Найди поле по локатору locator, очисти его и введи туда значение переменной text
        Args:
            locator (tuple): кортеж с локатором
            text (str): текст
        """
        input_element = self.find(locator)
        input_element.clear()
        input_element.send_keys(text)

    def get_text(self, locator):
        """Получает текст из элемента
        Args:
            locator (tuple): кортеж с локатором
        Returns:
            str: текст"""
        return self.find(locator).text

    def is_visible(self, locator):
        """Проверяет, что элемент виден на странице
        Args:
            locator (tuple): кортеж с локатором
        Returns:
            bool: True, если элемент виден, False в противном случае"""
        try:
            self.find(locator)
            return True
        except:
            return False

    def get_current_url(self):
        """Возвращает текущий URL страницы
        Returns:
            str: текущий URL страницы"""
        return self.driver.current_url


    def wait_for_tab_to_be_active(self, tab_text, timeout=10):
        """
        Явно ждёт, пока вкладка с нужным текстом станет активной.
        
        Args:
            tab_text (str): текст вкладки ("Булки", "Соусы", "Начинки")
            timeout (int): время ожидания в секундах
        """
        
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: any(
                    tab_text in el.text and 
                    'tab_tab_type_current' in el.get_attribute("class")
                    for el in d.find_elements(*HeaderLocators.TAB)
                ),
                message=f"Вкладка '{tab_text}' не стала активной за {timeout} секунд"
            )
            return True
        except TimeoutException:
            return False

    def switch_and_verify_tab(self, tab_locator, expected_text):
        """
        Кликает на вкладку и проверяет, что она стала активной
        
        Args:
            tab_locator: локатор вкладки
            expected_text: ожидаемый текст активной вкладки
        """
        self.click(tab_locator)
        assert self.wait_for_tab_to_be_active(expected_text), \
            f"Вкладка '{expected_text}' не активировалась"
        assert expected_text in self.get_text(HeaderLocators.ACTIVE_TAB), \
            f"Текст активной вкладки не соответствует '{expected_text}'"
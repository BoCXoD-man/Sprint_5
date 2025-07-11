# 🛸 Автотесты для Stellar Burgers

Автоматизированные UI-тесты для учебного веб-приложения [Stellar Burgers](https://stellarburgers.nomoreparties.site) — космического конструктора бургеров.

---

## 📌 Что проверяется

- ✅ Успешная и неуспешная регистрация
- ✅ Вход в систему (с разных точек)
- ✅ Переход в личный кабинет и обратно в конструктор
- ✅ Выход из аккаунта
- ✅ Переключение между вкладками конструктора: **Булки**, **Соусы**, **Начинки**

---

## ⚙️ Технологии

- Python 3.11+
- Selenium WebDriver
- Pytest

---

## 📁 Структура проекта

```text
Sprint_5/
├── .gitignore
├── conftest.py
├── constants.py
├── generator_log_pas.py        # генерация email и паролей
├── locators.py                 # все локаторы проекта
├── requirements.txt
├── README.md

├── pages/                      # Page Object модели
│   ├── base_page.py            # базовая логика работы с элементами
│   ├── login_page.py           # логика страницы логина
│   └── regis_page.py           # логика страницы регистрации

├── tests/                      # UI-тесты Pytest
│   ├── test_login.py           # тесты авторизации
│   ├── test_register.py        # тесты регистрации
│   └── test_profile_and_navigation.py  # тесты переходов и навигации
```

## 🚀 Как запустить

1. Установите зависимости:

```bash
pip install -r requirements.txt
```
Запустите тесты, находясь в директории проекта:

```bash
pytest -v # запустит все тесты

# А дальше запуски отдельных проверок: 
pytest -v tests\test_profile_and_navigation.py
pytest -v tests\test_login.py
pytest -v tests\test_register.py
```


## 🧠 Особенности

* Генерация email происходит автоматически (generator_log_pas.py)
* Все локаторы централизованы в locators.py
* Каждый тест изолирован: открывает браузер, выполняет действия и завершает сессию
* Используются фикстуры: например, login_user для авторизованного пользователя

A: По совету Константина (Наставника) в некоторых файлах по 2 ассерта: один проверяет нужный урл, второй наличие в нем видимого для авторизованного пользователя объекта того места, где он оказался. Речь шла о тестах раздела "вход".
Но я решил применить их и в навигации. Если они излишни где-то, не отправляйте на доработку из-за этого пункта, просто укажите в ОС , я их потом уберу.

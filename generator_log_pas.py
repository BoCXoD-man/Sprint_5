# генератор логина и пароля

import random
import string

def generate_email():
    """Генерирует адрес электронной почты, согласно требованиям.
    - имя_фамилия_номер когорты_любые 3 цифры@домен
    Пример: testtestov1999@yandex.ru.
    Returns:
        str: Адрес электронной почты.
    """
    name = "andrey"
    surname = "manaev"
    group = "29"
    random_digits = ''.join(random.choices(string.digits, k=3))
    return f"{name}_{surname}_{group}_{random_digits}@yandex.ru"

def generate_password(length=8):
    """ Генерирует пароль заданной длины, 
    состоящий из букв и цифр разных регистров.
    Args:
        length (int, optional): Длина пароля. По умолчанию 8.
    Returns:
        str: Генерированный пароль.
    """
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))


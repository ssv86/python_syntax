# Программа с графическим пользовательским интерфейсом (GUI)

# *** Генератор паролей ***

# импортирование необходимых модулей
import hashlib as h
from tkinter import Tk, Label, Entry, Button, StringVar

# основная функция
def pwdGenerator(pwd_str: str):
    # кодирование в байт-строку
    byte_str = pwd_str.encode()
    # хеширование
    hash_obj = h.sha256(byte_str)
    # преобразование хеш объекта в обычную строку
    hex_str = hash_obj.hexdigest()[:10]
    # возврат результата
    # print(hex_str)
    return hex_str

# тестирование
# pwdGenerator("qwerty")
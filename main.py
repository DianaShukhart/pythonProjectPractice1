
import math  # Подключение математического модуля

try:  # Защищенный блок 1
    b = float(input("Введите B="))
    d = float(input("Введите D="))
    x = float(input("Введите X="))
    try:  # Защищенный блок 2
        if x >= 8:
            y = (x-2)/(x**2)
        else:
            y= (b**2)*d+4*(x**2)
        print("y = %.1f" % y)

    except:  # Обработчик ошибок для защищенного блока 1
        print("Нет решения!")
except:  # Обработчик ошибок для защищенного блока 2
    print("Неверные входные данные!")
input("Нажмите Enter для выхода")  # Задержка перед выходом из программы



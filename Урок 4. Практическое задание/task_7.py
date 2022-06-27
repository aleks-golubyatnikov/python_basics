from itertools import count

"""
7. Реализовать генератор с помощью функции с ключевым словом yield,
 создающим очередное значение.

 При вызове функции должен создаваться объект-генератор.
 Функция должна вызываться следующим образом: for el in fact(n).
 Функция отвечает за получение факториала числа,
 а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

def my_fact(n):
    """
    Функция возвращает факториал числа
    :param n: Параметр - указание до какого числа посчитать факториал
    :return: Значение факториала
    """

    value = 1
    for i in count(1):
        if i > n:
            break
        else:
            value *= i

    yield value

try:
    number = int(input("Введите число: "))

except ValueError:
    print("Ошибка приеобразования аргумента к типу <int>")

i = 0
for el in my_fact(number):
    i += 1
    print(f"Число: {i}, факториал: {el}")


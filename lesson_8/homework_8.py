'''
======================================
1. Создай две функции: inner() и outer().
В inner() вызови деление на ноль.
В outer() просто вызови inner().
Попробуй вызвать outer() без обработки ошибок и посмотри на стек вызовов.

Сначала вызвался outer(), далее return inner() и потом уже return 10 / 0
======================================
'''
import math

def inner():
    return 10 / 0
def outer():
    return inner()
outer()
'''
======================================
2. Добавь вокруг вызова outer() конструкцию try/except,
чтобы перехватить исключение и вывести сообщение
"Ошибка перехвачена на верхнем уровне".
======================================
'''
def inner():
    return 10 / 0
def outer():
    return inner()

try:
    outer()
except ZeroDivisionError:
    print('Ошибка перехвачена на верхнем уровне')

'''
======================================
3. Перехвати исключение сразу в inner(), чтобы оно не поднималось дальше.
В случае ошибки возвращай строку "Ошибка в inner".
======================================
'''
def inner():
    try:
        return 10 / 0
    except ZeroDivisionError:
        print("Ошибка в inner")
def outer():
    return inner()
outer()
'''
======================================
4. Сделай так:
В inner() ошибка не перехватывается.
В outer() ошибка перехватывается через try/except.
В outer() при перехвате напечатай "Ошибка в outer".
======================================
'''
def inner():
    return 10 / 0
def outer():
    try:
        return inner()
    except ZeroDivisionError:
        print("Ошибка в outer")
outer()

'''
======================================
5. Напиши функцию get_value(), которая кидает ValueError.
Напиши тестовую функцию test_get_value(), которая:

Вызывает get_value();
Ловит ValueError;
Завершает тест с assert False, если исключение поймано.
======================================
'''
def get_value():
    raise ValueError

def test_get_value():
    try:
        get_value()
    except ValueError:
        assert False, 'Тест упал'

test_get_value()

'''
======================================
6. Создай функцию divide(x, y).
Если y == 0, выбрасывай ZeroDivisionError через raise.
Иначе возвращай результат деления.
======================================
'''
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    else:
        return x / y
divide(5, 0)

'''
======================================
7. Создай функцию sqrt(x), которая:
Вызывает raise NegativeNumberError (пользовательское исключение), если x < 0;
Иначе возвращает квадратный корень из x.
Проверь поведение функции через try/except.
======================================
'''
import math

class NegativeNumberError(Exception):
    pass

def sqrt(x):
    if x < 0:
        raise NegativeNumberError
    else:
        return math.sqrt(x)

try:
    print(sqrt(-10))
except NegativeNumberError:
    print('Вы ввели негативное число')

'''
======================================
8. Создай базовый класс MathError.
От него унаследуй:
NegativeNumberError
DivisionByZeroError
В функции safe_divide(x, y) выбрасывай DivisionByZeroError, если y == 0.
Проверь в try/except обработку ошибок через базовый класс MathError.
======================================
'''
class MathError(Exception):
    pass
class NegativeNumberError(MathError):
    pass
class DivisionByZeroError(MathError):
    pass

def safe_divide(x, y):
    if y == 0:
        raise DivisionByZeroError("Деление на ноль")
    else:
        return x / y

try:
    print(safe_divide(5, 0))
except MathError as e:
    print(f'Математическая ошибка: {e}')
'''
======================================
9. Создай тестовую функцию test_sqrt(), которая:
вызывает sqrt(x) с отрицательным числом;
перехватывает NegativeNumberError;
завершает тест с assert False и сообщением
"Нельзя брать корень из отрицательного числа".
======================================
'''
def test_sqrt():
    try:
        sqrt(-5)
    except NegativeNumberError:
        assert False, 'Нельзя брать корень из отрицательного числа'
test_sqrt()

'''
======================================
10. Открой файл sample.txt, прочитай его содержимое и выведи на экран.
Обеспечь закрытие файла через with.
======================================
'''
with open('sample.txt') as f:
    for line in f:
        print(line, end="")

'''
======================================
11. Создай класс BackupList, который:
делает копию списка при входе в with,
при выходе сохраняет изменения, если ошибок не было,
откатывает изменения при ошибке.
Проверь:
успешное изменение списка;
откат при ошибке.
======================================
'''
class BackupList:
    def __init__(self, lst):
        self.lst = lst

    def __enter__(self):
        self.copy_lst = self.lst.copy()
        return self

    def append_lst_str(self, value):
        if not isinstance(value, str):
            raise ValueError('В лист можно добавить только строку')
        self.lst.append(value)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('Ошибок не было, список успешно сохранен')
        else:
            print('Список сохранить не удалось')
            self.lst.clear()
            self.lst.extend(self.copy_lst)
            print(f"Ошибка: {exc_type.__name__}: {exc_val}")
        return True

lst_1 = ['test', 'test1', 1, 'test 2']
with BackupList(lst_1) as b:
    b.append_lst_str(1)
print(lst_1)

'''
======================================
12. Создай декоратор-класс Timer,
который измеряет время выполнения функции и выводит результат.
======================================
'''
import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result

@Timer
def test():
    time.sleep(1)
    print('Что-то')

test()


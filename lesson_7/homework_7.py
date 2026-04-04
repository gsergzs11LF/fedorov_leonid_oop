'''
Домашка по 7 уроку
'''


"""
======================================
1. Создай три класса: Cat, Dog, Duck.
В каждом реализуй метод speak(), возвращающий уникальную строку.
Создай список из экземпляров этих классов и вызови метод speak()
в цикле.
======================================
"""
class Cat:
    def speak(self):
        return 'Кошка говорит "мяу"'
class Dog:
    def speak(self):
        return 'Собака говорит "гав"'
class Duck:
    def speak(self):
        return 'Утка говорит "кря"'

animals = [Cat(), Dog(), Duck()]
for animal in animals:
    print(animal.speak())

"""
======================================
2. Создай базовый класс Shape
Создай три класса-наследника: Square, Rectangle, Triangle,
в каждом реализуй метод get_pr().
Проверь, что список shapes = [Square(...), Rectangle(...), Triangle(...)]
можно обойти в цикле и вызвать get_pr() у каждого.
======================================
"""

class Shape:
    def __init__(self, a):
        self.a = a
    def get_pr(self):
        pass

class Square(Shape):
    def get_pr(self):
        return f'Периметр квадрата = {self.a * 4}'

class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b
    def get_pr(self):
        return f'Периметр прямоугольника = {2 * (self.a + self.b)}'

class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__(a)
        self.b = b
        self.c = c
    def get_pr(self):
        return f'Периметр треугольника = {self.a + self.b + self.c}'

shapes = [Square(5), Rectangle(3, 7), Triangle(3, 3, 5)]
for shape in shapes:
    print(shape.get_pr())



"""
======================================
3. Сделай класс Shape абстрактным.
Переопредели get_pr() как @abstractmethod.
Попробуй создать объект класса Shape напрямую и убедись, что будет TypeError.
======================================
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_pr(self):
        pass

class Square(Shape):
    def __init__(self, a):
        self.a = a
    def get_pr(self):
        return f'Периметр квадрата = {self.a * 4}'

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_pr(self):
        return f'Периметр прямоугольника = {2 * (self.a + self.b)}'

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def get_pr(self):
        return f'Периметр треугольника = {self.a + self.b + self.c}'

shapes = Shape()

"""
======================================
4. Создай классы A, B, C, в каждом — свой __init__() с print("init A/B/C").
Наследуй D(A, B, C) и вызови super().__init__() в каждом __init__.
Выведи D.__mro__ и посмотри, в каком порядке вызываются инициализаторы.
======================================
"""
class A:
    def __init__(self):
        print("init A")
        super().__init__()
class B:
    def __init__(self):
        print("init B")
        super().__init__()

class C:
    def __init__(self):
        print("init C")
        super().__init__()

class D(A, B, C):
    def __init__(self):
        super().__init__()
d = D()
print(D.__mro__ )

"""
======================================
5. Создай MixinLog (как в уроке).
Создай класс бронирования гостиницы (методы и атрибуты на свое усмотрение).
Создай класс, который наследует оба класса. Создай экземпляр этого класса.
======================================
"""
import datetime
class Booking:
    def __init__(self, b_id: int ,room: int, price: int, date: str, deposit: bool):
        self.b_id = b_id
        self.room = room
        self.price = price
        self.date = date
        self.deposit = deposit
        super().__init__()
    def change_date(self, new_date: str):
        self.date = new_date

class MixinLOG:
    def __init__(self):
        super().__init__()
        print(f'Бронь создана. Дата создания - {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    def book_info(self):
        print(
            "Информация о брони:\n"
            f"<ID - {self.b_id}>\n"
            f"<Количество комнат - {self.room}>\n"
            f"<Цена - {self.price}>\n"
            f"<Дата заезда - {self.date}>\n"
            f"<Внесен ли депозит - {self.deposit}>"
        )

class TestBook(Booking, MixinLOG):
    pass

b_1 = TestBook(1, 5,5000, "25 марта", True)
b_1.book_info()

"""
======================================
6. В Goods и MixinLog реализуй print_info().
Создай NoteBook(Goods, MixinLog) и проверь, какой метод вызывается.
Измени порядок наследования — изменилась ли логика?
======================================
да, логика изменится так как мы поменяли порядок наследования и метод теперь ищется в другом порядке
если добавить super() то можно вызывать оба и первый по порядку наследования и следующий
"""
class Goods:
    def print_info(self):
        print('Какая-то информация из класса Goods')
class MixinLog:
    def print_info(self):
        print('Какая-то информация из класса MixinLog')
class NoteBook(MixinLog, Goods):
    pass
n = NoteBook()
n.print_info()

"""
======================================
7. Напиши программу, которая запрашивает (из консоли) два числа и делит первое на второе.
Если второе число равно нулю — обработай ошибку (как называется ошибка найди сам)
и выведи сообщение: "На ноль делить нельзя!"
ZeroDivisionError
======================================
"""
try:
    x = float(input('Введи первое число:'))
    y = float(input('Введи второе число:'))
    try:
        z = x / y
        print('Результат деления:', z)
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
except ValueError:
    print('Введен не верный тип данных')

"""
======================================
8. Расширь программу из Задания 1:
Добавь обработку ошибки (как называется ошибка найди сам),
если пользователь ввёл не числа, а текст.
Выведи сообщение: "Ошибка ввода: введите два числа через пробел"
======================================
"""
try:
    inp = input('Введи два числа через пробел:')
    x, y = inp.split(' ')
    z = int(x) / int(y)
    print('Результат деления:', z)
except ZeroDivisionError:
        print("На ноль делить нельзя!")
except ValueError:
    print("Ошибка ввода: введите два числа через пробел")

"""
======================================
9. Модифицируй код так, чтобы после обработки конкретных ошибок
был ещё один общий except, который перехватывает все остальные ошибки и выводит:
"Произошла неизвестная ошибка"
======================================
"""
try:
    inp = input('Введи два числа через пробел:')
    x, y = inp.split(' ')
    z = int(x) / int(y)
    print('Результат деления:', z)
except ZeroDivisionError:
        print("На ноль делить нельзя!")
except ValueError:
    print("Ошибка ввода: введите два числа через пробел")
except:
    print('Произошла неизвестная ошибка')

"""
======================================
10. При перехвате исключений из 7 и 8 заданий,
сохрани ошибку в переменную e и выведи её текст:
======================================
"""
try:
    inp = input('Введи два числа через пробел:')
    x, y = inp.split(' ')
    z = int(x) / int(y)
    print('Результат деления:', z)
except ZeroDivisionError as e:
        print("На ноль делить нельзя!", e)
except ValueError as v:
    print("Ошибка ввода: введите два числа через пробел", v)
except:
    print('Произошла неизвестная ошибка')

"""
======================================
11. Создай код, который ловит арифметические ошибки (ArithmeticError) в одном блоке.
Попробуй специально сделать ошибку деления на ноль или другую арифметическую ошибку.
======================================
"""
try:
    inp = input('Введи два числа через пробел:')
    x, y = inp.split(' ')
    z = int(x) / int(y)
    print('Результат деления:', z)
except ArithmeticError as a:
        print("Арифметическая ошибка: ", a)
except ValueError as v:
    print("Ошибка ввода: введите два числа через пробел", v)
except:
    print('Произошла неизвестная ошибка')

"""
======================================
12. Запроси у пользователя два числа и выполни деление.
Если деление прошло успешно без ошибок — выведи
"Деление выполнено успешно" через (но не в блоке try)
======================================
"""
try:
    inp = input('Введи два числа через пробел:')
    x, y = inp.split(' ')
    z = int(x) / int(y)
except ArithmeticError as a:
        print("Арифметическая ошибка: ", a)
except ValueError as v:
    print("Ошибка ввода: введите два числа через пробел", v)
except:
    print('Произошла неизвестная ошибка')
else:
    print("Деление выполнено успешно, результат деления: ", z)
"""
======================================
13. Расширь код из Задания 12:
Добавь блок, в котором будет выводиться
"Работа программы завершена", независимо от успеха деления.
======================================
"""
try:
    inp = input('Введи два числа через пробел:')
    x, y = inp.split(' ')
    z = int(x) / int(y)
except ArithmeticError as a:
        print("Арифметическая ошибка: ", a)
except ValueError as v:
    print("Ошибка ввода: введите два числа через пробел", v)
except:
    print('Произошла неизвестная ошибка')
else:
    print("Деление выполнено успешно, результат деления: ", z)
finally:
    print("Работа программы завершена")

"""
======================================
14. Реализуй две вложенные конструкции:
Внешний try/except обрабатывает неверный ввод (строки вместо чисел);
Внутренний try/except ловит деление на ноль.
======================================
"""
try:
    inp = input('Введи два числа через пробел:')
    x, y = inp.split(' ')

    try:
        z = int(x) / int(y)
    except ZeroDivisionError as a:
            print("Нельзя делить на ноль: ", a)

except ValueError as v:
    print("Ошибка ввода: введите два числа через пробел", v)

except:
    print('Произошла неизвестная ошибка')
else:
    print("Деление выполнено успешно, результат деления: ", z)
finally:
    print("Работа программы завершена")

"""
======================================
15. Вынеси обработку деления в отдельную функцию divide(x, y)
с собственным try/except.
Во внешнем коде обработай только ошибку ввода.
======================================
"""

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as a:
        print("Нельзя делить на ноль: ", a)

try:
    inp = input('Введи два числа через пробел:')
    x, y = map(int, inp.split(' '))
    res = divide(x, y)
except ValueError as v:
    print("Ошибка ввода: введите два числа через пробел", v)

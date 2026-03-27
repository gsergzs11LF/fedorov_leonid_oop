'''
ДЗ по третьему уроку
'''

"""
======================================
1. Создай класс Circle, в котором:
есть атрибуты класса MIN_RADIUS = 1 и MAX_RADIUS = 1000,
метод класса is_valid_radius(cls, r), который проверяет, входит ли значение в допустимый диапазон.
Проверь результат вызова:
print(Circle.is_valid_radius(500))   # True
print(Circle.is_valid_radius(1500))  # False
======================================
"""

# class Circle:
#     MIN_RADIUS = 1
#     MAX_RADIUS = 1000
#
#     @classmethod
#     def is_valid_radius(cls, r: int):
#         return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS
#
# print(Circle.is_valid_radius(500))

"""
======================================
2. Добавь в класс Circle:
статический метод area(radius),
который возвращает площадь круга по формуле π * r ** 2 (используй импорт math.pi),
инициализацию в __init__, которая сохраняет радиус,
только если он проходит валидацию через метод is_valid_radius()
(подумай как можно проверить значения перед тем как записать их в переменные экземпляра класса)
Пример:
c = Circle(10)
print(c.area(c.radius))  # Площадь круга
======================================
"""
# from math import pi
#
# class Circle:
#     MIN_RADIUS = 1
#     MAX_RADIUS = 1000
#
#     def __init__(self, radius: int):
#         if self.is_valid_radius(radius):
#             self.radius = radius
#
#     @classmethod
#     def is_valid_radius(cls, r: int):
#         return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS
#
#     @staticmethod
#     def area(radius):
#         return pi * radius ** 2
#
# c = Circle(10)
# print(c.radius)
# print(c.area(c.radius))

"""
======================================
3. Расширь Circle, добавив обычный метод print_info, который выводит:
Радиус: ...
Допустимый диапазон: [MIN, MAX]
Метод должен использовать и self, и атрибуты класса через type(self).

Пример вызова:
c.print_info()
======================================
"""

from math import pi

class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    def __init__(self, radius: int):
        if self.is_valid_radius(radius):
            self.radius = radius

    @classmethod
    def is_valid_radius(cls, r: int):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

    @staticmethod
    def area(radius):
        return pi * radius ** 2

    def print_info(self):
        print('Радиус: ', c.radius)
        print(f"Допустимый диапазон: [{type(self).MIN_RADIUS}:{type(self).MAX_RADIUS}]")


c = Circle(10)
print(c.radius)
print(c.area(c.radius))
c.print_info()

"""
======================================
4. Создай класс User, в котором:

приватные атрибуты __login и __password;
метод set_credentials(login, password), который сохраняет их только если оба значения — строки;
метод get_credentials(), который возвращает кортеж из логина и пароля.
Попробуй создать объект и изменить логин снаружи напрямую. Проверь, что это не сработает.
======================================
"""

# class User:
#     def __init__(self):
#         self.__login = None
#         self.__password = None
#     def set_credentials(self, login: str, password: str):
#         if isinstance(login, str) and isinstance(password, str):
#             self.__login = login
#             self.__password = password
#     def get_credentials(self) -> tuple[str, str]:
#         return self.__login, self.__password
#
# user_1 = User()
# user_1.set_credentials('sfsdf@ss.sdf','qwerty123456')
# print(user_1.get_credentials())
#
# user_1.login = 'qwerty321'
# print(user_1.get_credentials())
# print(user_1.__dict__)

"""
======================================
5. Добавь в User:

метод check_password(password) — возвращает True,
если переданное значение совпадает с сохранённым паролем;
приватный метод __encrypt_password(password),
который возвращает пароль в верхнем регистре (имитация шифрования);
в set_credentials вызывай __encrypt_password.
Пример:
u = User()
u.set_credentials("daniil", "qwerty")
print(u.check_password("qwerty"))      # True
print(u.check_password("qwe"))         # False
======================================
"""

class User:
    def __init__(self):
        self.__login = None
        self.__password = None

    def set_credentials(self, login: str, password: str):
        if isinstance(login, str) and isinstance(password, str):
            self.__login = login
            self.__password = self.__encrypt_password(password)

    def get_credentials(self) -> tuple[str, str]:
        return self.__login, self.__password

    def check_password(self, password: str) -> bool:
        return  self.__password == self.__encrypt_password(password)

    @staticmethod
    def __encrypt_password(password: str) -> str:
        return  password.upper()


u = User()
u.set_credentials("daniil", "qwerty")
print(u.check_password("qwerty"))      # True
print(u.check_password("qwe"))      # False

"""
======================================
6. Убедись, что приватный метод __encrypt_password нельзя вызвать извне.
Попробуй это сделать — и поясни результат.
Также выведи напрямую u.__password — и проверь, что будет ошибка.

Попробуй добраться до данных через u._User__password
======================================
"""
# u.__encrypt_password("test")
print(u._User__encrypt_password('fsdf')) # - Преобразует введенную строку в верхний регистр
"""
получаем ошибку 'User' object has no attribute '__encrypt_password'. Did you mean: '_User__encrypt_password'?
Когда мы добавили __ перед encrypt_password то метод превратился в _User__encrypt_password. То есть мы его спрятали
Тоже самое будет и с u.__password - 'User' object has no attribute '__password'
"""
# print(u.__password) # - ошибка
print(u._User__password) # - выведет сохраненный пароль
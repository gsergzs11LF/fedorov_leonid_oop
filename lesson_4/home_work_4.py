'''
======================================
1. Создай класс SecureData, который:

имеет атрибут __secret, задаваемый в __init__;
переопределяет __getattribute__, чтобы при попытке получить __secret извне выбрасывать ValueError;
внутри класса доступ к __secret должен работать.
Проверь:
data = SecureData("пароль123")
print(data.__secret)      # ошибка
print(data.get_secret())  # "пароль123"
======================================
'''


# class SecureData:
#     def __init__(self, secret):
#         self.__secret = secret
#
#     def __getattribute__(self, item):
#         if item == '_SecureData__secret':
#             raise ValueError ('Значение засекречено')
#         return object.__getattribute__(self, item)
#
#     def get_secret(self):
#         return self.__secret
#
# data = SecureData("пароль123")
# print(data.__secret)
# # print(data.get_secret())

'''
======================================
2. Добавь в класс SecureData метод __setattr__,
который запрещает создание любого атрибута с именем token.

Проверь:
data.token = "abc123"  # ❌ AttributeError
data.other = "ok"      # ✅ работает
======================================
'''
# class SecureData:
#     def __init__(self, secret):
#         self.__secret = secret
#
#     def __getattribute__(self, item):
#         if item == '__secret':
#             raise ValueError ('Значение засекречено')
#         return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#         if key == 'token':
#             raise AttributeError (f"Невозможно создать атрибут с именем {key}")
#         return object.__setattr__(self, key, value)
#
#     def get_secret(self):
#         return self.__secret
#
#
# data = SecureData("пароль123")
# # data.token = "abc123"
# data.other = "ok"
# print(data.other)

'''
======================================
3. Создай класс SafeDict, в котором:

нет атрибута default;
реализован __getattr__, который возвращает "N/A" (это строка) при попытке получить несуществующий атрибут;
реализован __delattr__, который пишет "Удалён атрибут <имя>" и действительно удаляет атрибут.
Проверь:
d = SafeDict()
print(d.unknown)     # "N/A"
d.key = 10
del d.key            # "Удалён атрибут key"
======================================
'''
# class SafeDict:
#     def __getattr__(self, item):
#         return 'N/A'
#     def __delattr__(self, item):
#         print(f'Удален атрибут {item}')
#         return object.__delattr__(self, item)
#
# d = SafeDict()
# print(d.unknown)     # "N/A"
# d.key = 10
# del d.key            # "Удалён атрибут key"

'''
======================================
4. Создай класс Employee с приватными полями __name и __salary.
Добавь @property для поля salary, а также сеттер с валидацией:

зарплата должна быть положительным числом;
если нет — выбрасывать ValueError.
Проверь, что:
e = Employee("Daniil", 5000)
print(e.salary)   # 5000
e.salary = 8000
print(e.salary)   # 8000
e.salary = -100   # ❌ ValueError
======================================
'''
# class Employee:
#     def __init__(self, name: str, salary: int):
#         self.__name = name
#         self.salary = salary
#
#     @property
#     def salary(self):
#         return self.__salary
#     @salary.setter
#     def salary(self, value):
#         if value <= 0:
#             raise ValueError('Зарплата не может быть меньше нуля')
#         self.__salary = value
#
# e = Employee("Daniil", 5000)
# print(e.salary)   # 5000
# e.salary = 8000
# print(e.salary)   # 8000
# e.salary = -100   # ❌ ValueError

'''
======================================
5. Добавь @deleter для поля salary, чтобы при удалении выводилось "зарплата удалена"
и поле реально исчезало.
Проверь:

del e.salary
print(e.__dict__)  # salary нет
======================================
'''
#
# class Employee:
#     def __init__(self, name: str, salary: int):
#         self.__name = name
#         self.salary = salary
#
#     @property
#     def salary(self):
#         return self.__salary
#     @salary.setter
#     def salary(self, value):
#         if value < 0:
#             raise ValueError('Зарплата не может быть меньше нуля')
#         self.__salary = value
#     @salary.deleter
#     def salary(self):
#         print('зарплата удалена')
#         del self.__salary
#
# e = Employee("Daniil", 5000)
# del e.salary
# print(e.__dict__)

'''
======================================
6. Представь, что ты пишешь обёртку над HTML-формой.
Создай класс LoginForm с полем username, которое реализовано через @property.

Логика:
геттер возвращает self._username
сеттер добавляет лог "username изменён"
Проверь, что:
form = LoginForm()
form.username = "admin"  # выводит лог
print(form.username)     # "admin"
======================================
'''
# class LoginForm:
#     def __init__(self):
#         self._username = None
#     @property
#     def username(self):
#         return self._username
#     @username.setter
#     def username(self, value):
#         print('Username был изменён')
#         self._username = value
#
# form = LoginForm()
# form.username = "admin"  # выводит лог
# print(form.username)     # "admin"

'''
======================================
7. Создай класс Card, где:
поле __number хранит номер карты (строка);
в @property возвращай номер с маской **** **** **** 1234;
в @setter проверяй, что номер состоит из 16 цифр;
в @deleter логируй удаление номера с текущим временем.
Напиши тесты (через assert)
проверку установки корректного номера;
проверку исключения при вводе короткого номера;
проверку вывода замаскированного номера.
======================================
'''
# from datetime import datetime
# class Card:
#     def __init__(self, number: str):
#         self.number = number
#     @property
#     def number(self):
#         return '**** **** **** ' + self.__number[-4:]
#     @number.setter
#     def number(self, value):
#         if not (len(value) == 16 and value.isdigit()):
#             raise ValueError ('Номер карты должен состоять строго из 16 цифр')
#         self.__number = value
#     @number.deleter
#     def number(self):
#         print(f"[LOG] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.\nНомер карты {self.number} был удален")
#         del self.__number
#
# c = Card('0000000000001234')
# print(c.number)
#
# assert c._Card__number == "0000000000001234", "Установлен не корректный номер карты"
#
# try:
#     Card('1234')
#     assert False, 'Проверка на номер карты не сработала'
# except ValueError:
#     assert True
#
# assert c.number == "**** **** **** 1234", "Номер выводится без маскировки"

'''
======================================
8. Создай класс UserData для API регистрации пользователя:
email — строка, содержит @;
age — целое число ≥ 18;
is_active — bool;
свойство .json возвращает словарь для запроса.
Напиши тест (через assert)
проверь, что при age = 15 выбрасывается ValueError;
проверь, что email без @ вызывает ошибку;
проверь, что json возвращает корректную структуру.
======================================
'''

class UserData:
    def __init__(self, email: str, age: int, is_active: bool):
        self.email = email
        self.age = age
        self.is_active = is_active

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value: str):
        if not '@' in value:
            raise ValueError (f"В почте '{value}' отсутствует '@'")
        self._email = value

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value: int):
        if not (value >= 18 and isinstance(value, int)):
            raise ValueError(f"Возраст - '{value}' не целое число или меньше 18 ")
        self._age = value

    @property
    def is_active(self):
        return self._is_active
    @is_active.setter
    def is_active(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError(f"Введенное значение - '{value}' не булево число ")
        self._is_active = value

    def json(self):
        return {
            'email' : self.email,
            'age' : self.age,
            'is_active' : self.is_active
        }

u = UserData('sdf@mail.ru', 23, True)

try:
    UserData('sdf@mail.ru', 15, True)
    assert False, 'ValueError не выбрасывается'
except ValueError:
    assert True
    print('ValueError выбрасывается')

try:
    UserData('sdfmail.ru', 23, True)
    assert False, 'Email без собаки ошибку не вызвал'
except ValueError:
    assert True
    print('Email без собаки вызывает ошибку ValueError')

assert u.json() == {'email': 'sdf@mail.ru', 'age': 23, 'is_active': True}, 'Словарь приходит не в том виде'


"""
------------------------------------------------------------------------------------------------------------------------
                                    Методы класса и статические методы
------------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------------
📘 @classmethod и @staticmethod в Python
------------------------------------------------------------------------------------------------------------------------
🔹 @classmethod
Определение:
Метод класса — работает с классом, а не с объектом.

Аргумент:
cls — ссылка на класс

Особенности:
имеет доступ к атрибутам класса
может создавать объекты (cls(...))
вызывается через класс или объект

Синтаксис:
@classmethod
def method(cls, ...):
    ...

Пример:
class User:
    def __init__(self, name):
        self.name = name
    @classmethod
    def create(cls, name):
        return cls(name)

u = User.create("Alex")
------------------------------------------------------------------------------------------------------------------------
🔹 @staticmethod

Определение:
Статический метод — обычная функция внутри класса.

Аргументы:
нет self, нет cls

Особенности:
не имеет доступа к классу и объекту
используется как вспомогательная функция
вызывается через класс или объект

Синтаксис:

@staticmethod
def method(...):
    ...

Пример:

class User:
    @staticmethod
    def is_valid_name(name):
        return len(name) > 0

User.is_valid_name("Alex")
------------------------------------------------------------------------------------------------------------------------
"""

class BankAccount:
    MIN_BALANCE = 0
    MAX_BALANCE = 1_000_000

    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: int):
        self.balance += amount

    @classmethod
    def demo(cls):
        return cls(owner='Test', balance=10_000)

    @classmethod
    def validate_balance(cls, balance: int):
        return cls.MIN_BALANCE <= balance <= cls.MAX_BALANCE

    @staticmethod
    def calc_percent(balance: int, rate: int):
        return balance * (rate / 100)


ba = BankAccount.demo()
print(ba.owner)
print(ba.balance)
ba.deposit(-100)
print(ba.balance)
print(ba.validate_balance(ba.balance))

print(BankAccount.calc_percent(100, 23))


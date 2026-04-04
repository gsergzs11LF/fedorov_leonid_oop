'''
------------------------------------------------------------------------------------------------------------------------
                              Управление приватными аттрибутами через @property
------------------------------------------------------------------------------------------------------------------------
'''

'''
Вариант без @property - тут get_balance и set_balance используются как методы, их нужно постоянно вызывать
'''
# class BankAccount:
#     BANK_NAME = "Легко в ИТ Банк"  # - атрибут класса
#     MIN_BALANCE = 0  # - атрибут класса
#
#     def __init__(self, owner: str, balance: int):
#         self.__owner = owner  # - атрибут экземпляра
#         self.__balance = balance # - атрибут экземпляра
#
#     def get_balance(self): # - создали метод, который возвращает приватный атрибут
#         return self.__balance
#
#     def set_balance(self, value): # - создали метод, который меняет значение приватному атрибуту
#         self.__balance = value
#
# a1 = BankAccount('Leonid', 1000)
# print(a1.get_balance())
# a1.set_balance(200)
# print(a1.get_balance())

'''
Вариант с @property - 
'''

class BankAccount:
    BANK_NAME = "Легко в ИТ Банк"   # атрибут класса (общий для всех)
    MIN_BALANCE = 0                 # минимально допустимый баланс

    def __init__(self, owner: str, balance: int):
        self.__owner = owner        # приватный атрибут владельца
        self.__balance = balance    # приватный баланс (напрямую трогать нельзя)

    @property
    def balance(self):
        # вызывается при a1.balance
        # просто возвращаем текущее значение
        return self.__balance

    @balance.setter
    def balance(self, value):
        # вызывается при a1.balance = value
        
        # проверка: нельзя установить баланс меньше минимального
        if value < self.MIN_BALANCE:
            raise ValueError(f'Баланс не может быть меньше, чем {self.MIN_BALANCE}')

        # если всё ок — записываем значение
        # ВАЖНО: пишем в __balance, а не в balance (иначе рекурсия)
        self.__balance = value



a1 = BankAccount('Leonid', 1000)
print(a1.balance)
a1.balance = 111
print(a1.balance)


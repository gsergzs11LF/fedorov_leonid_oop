from datetime import datetime


class BookingData:
    def __init__(
            self,
            firstname: str,
            lastname: str,
            total_price: int,
            deposit_paid: bool,
    ):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__total_price = total_price
        self.__deposit_paid = deposit_paid
        self.created_at = datetime.now()

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, value):
        if not isinstance(value, str) or not value.isalpha():
            raise ValueError('Имя должно содержать только буквы')
        self.__firstname = value


    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        if not isinstance(value, str) or not value.isalpha():
            raise ValueError('Фамилия должна содержать только буквы')
        self.__lastname = value


    @property
    def total_price(self):
        return self.__total_price

    @total_price.setter
    def total_price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError('Цена должна быть положительным числом')
        self.__total_price = value


    @property
    def deposit_paid(self):
        return self.__deposit_paid

    @deposit_paid.setter
    def deposit_paid(self, value):
        if not isinstance(value, bool):
            raise ValueError('Депозит может быть только булевым значением')
        self.__deposit_paid = value


    @property
    def json(self):
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'total_price': self.total_price,
            'deposit_paid': self.deposit_paid,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

booking = BookingData('Leonid', 'Fedorov', 500, True)

assert booking.firstname == 'Leonid', 'Имя не верное'
assert booking.lastname == 'Fedorov', 'Фамилия не верная'
assert booking.json['deposit_paid'] is True









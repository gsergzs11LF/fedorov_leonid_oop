'''
ДЗ по уроку 2
'''

'''
======================================
1. Создай класс Person с методом set_data(self, name, age), который сохраняет имя и возраст в объект.
Добавь метод get_data(self), который возвращает строку вида "Имя: <name>, Возраст: <age>".
Создай два объекта и задай им разные значения. Выведи информацию по каждому.
======================================
'''
class Person:
    def set_data(self, name: str, age: int):
        self.name = name
        self.age = age
    def get_data(self):
        return f'Имя: {self.name}, возраст: {self.age}'

user_1 = Person()
user_2 = Person()
user_1.set_data('Lenid', 23)
user_2.set_data('Anastasia', 23)
print(user_1.get_data())
print(user_2.get_data())

'''
======================================
2. Добавь в класс Point методы set_coords(x, y) и get_coords().
Создай объект p, задай координаты (7, 12), а затем получи и выведи их.
После этого измени координаты на (-3, 5) и снова выведи результат через get_coords().
======================================
'''
class Point:
    def set_coords(self, x: int, y: int):
        setattr(self, "x", x)
        setattr(self, "y", y)
    def get_coords(self):
        return getattr(self, 'x'), getattr(self, 'y')

p = Point()
p.set_coords(7, 12)
print(p.get_coords())
setattr(p, 'x', -3)
setattr(p, 'y', 5)
print(p.get_coords())

'''
======================================
3. Используя getattr(), получи ссылку на метод get_coords у объекта Point и вызови его.
Проверь, что результат совпадает с обычным вызовом p.get_coords().
======================================
'''
res = getattr(p, 'get_coords')
print(res())

'''
======================================
4. Создай класс Person, в котором метод __init__() принимает имя и возраст и сохраняет их как атрибуты объекта.
Добавь метод show_info(), который выводит строку "Имя: <name>, возраст: <age>". Создай объект и вызови метод.
======================================
'''
# class Person1:
#     def __init__(self, name: str = 'Leonid123', age: int = 23123):
#         self.name = name
#         self.age = age
#     def show_info(self):
#         return f'Имя: {self.name}, Возраст: {self.age}'
#
# user_3 = Person1()
# print(user_3.show_info())

'''
======================================
5. Добавь в класс Person метод __del__(), который выводит сообщение "Удалён объект: <имя>",
где <имя> — значение поля name. Создай и удали объект вручную с помощью del.
======================================
'''
class Person1:
    def __init__(self, name: str = 'Leonid123', age: int = 23123):
        self.name = name
        self.age = age
    def show_info(self):
        return f'Имя: {self.name}, Возраст: {self.age}'
    def __del__(self):
        print(f'Удален объект {self.name}')

user_3 = Person1()
print(user_3.show_info())
del user_3

'''
======================================
6. Создай класс Rectangle с инициализацией по умолчанию: ширина 1, высота 1.
Добавь метод area(), который возвращает площадь прямоугольника.
Проверь работу с прямоугольником без аргументов и с заданной шириной и высотой.
======================================
'''
class Rectangle:
    def __init__(self, width: int = 1, height: int = 1):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

rectangle_1 = Rectangle()
rectangle_2 = Rectangle(5, 10)
print(rectangle_1.area())
print(rectangle_2.area())

'''
======================================
7. Создай класс Logger, который всегда возвращает один и тот же объект.
При создании экземпляра в __new__ выводи Создание логгера,
а при вызове __init__ — Инициализация логгера.
======================================
'''
class Logger:
    instance = None
    def __new__(cls, *args, **kwargs):
        print('Создание логгера')
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    def __init__(self):
        print('Инициализация логгера')

logger = Logger()
logger_2 = Logger()
print(id(logger))
print(id(logger_2))




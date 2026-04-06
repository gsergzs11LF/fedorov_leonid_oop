'''
Homework 6
'''

'''
======================================
1. Создай базовый класс Shape с методом area(), который возвращает 0.
Отнаследуй два класса: Circle и Square.
Переопредели метод area() так, чтобы он возвращал площадь круга или квадрата.

c = Circle(5)
s = Square(4)

print(c.area())  # ~78.5
print(s.area())  # 16
======================================
'''
from math import pi
class Shape:
    def __init__(self, value: int):
        self.value = value
    def area(self):
        return 0

class Circle(Shape):
    def area(self):
        return round(pi * self.value ** 2, 1)

class Square(Shape):
    def area(self):
        return self.value ** 2

c = Circle(5)
s = Square(4)

print(c.area())  # ~78.5
print(s.area())  # 16

'''
======================================
2. Создай базовый класс BasePage с методом open(url).
Сделай добавь магический init, в котором указан текст на странице (любой)
От него унаследуй LoginPage и добавь метод find(text).
Проверь, что методы из базового класса тоже доступны:
page = LoginPage()
page.open("https://example.com/login")
page.find("Зима")
Вывод в консоли:
На странице найден текст: "Зима"

немного не понял суть задания
======================================
'''
class BasePage:
    def __init__(self, page_text):
        self.page_text = page_text

    def open(self, url: str):
        print(f'Открыта страница "{url}"')

class LoginPage(BasePage):
    def find(self, text: str):
        if text in self.page_text:
            print(f'На странице найден текст: "{text}"')

page = LoginPage('Зима')
print(page.page_text)
page.open("https://example.com/login")
page.find("Зима")

'''
======================================
3. Создай свой класс ResultList,
который наследует list и добавляет метод success_count(),
возвращающий количество успешных результатов (где item["status"] == "passed").

results = ResultList([
    {"status": "passed"},
    {"status": "failed"},
    {"status": "passed"},
])

print(results.success_count())  # 2
======================================
'''
class ResultList(list):
    def success_count(self):
        count = 0
        for item in self:
            if item['status'] == 'passed':
                count += 1
        return count

results = ResultList([
    {"status": "passed"},
    {"status": "failed"},
    {"status": "passed"},
])
print(results.success_count())

'''
======================================
4. Создай классы BaseStep и LoginStep, отнаследуй второй от первого.
 Создай объект step = LoginStep()
 Проверь, что он является экземпляром и LoginStep, и BaseStep, и object.

print(issubclass(LoginStep, BaseStep))  # True
print(isinstance(step, BaseStep))       # True
print(isinstance(step, object))         # True
======================================
'''
class BaseStep:
    pass

class LoginStep(BaseStep):
    pass

step = LoginStep()
print(issubclass(LoginStep, BaseStep))  # True
print(isinstance(step, LoginStep))      # True
print(isinstance(step, BaseStep))       # True
print(isinstance(step, object))         # True

'''
======================================
5. Создай класс ExtendedDict, который наследуется от dict,
и переопредели __str__, чтобы словарь красиво выводился в формате:
ключ: значение
ключ: значение
Пример:
d = ExtendedDict(a=1, b=2)
print(d)
Ожидаемый вывод:
a: 1
b: 2
======================================
'''
class ExtendedDict(dict):
    def __str__(self):
        return "\n".join(f"{k}: {v}" for k, v in self.items())

d = ExtendedDict(a=1, b=2)
print(d)

'''
======================================
6. Создай два класса:

Widget: принимает x, y и сохраняет как self.x, self.y;
Button: наследует Widget, добавляет label, но обязательно вызывает super().
Проверь, что всё сохраняется корректно.

btn = Button(100, 200, "OK")
print(btn.x, btn.y, btn.label)  # 100 200 OK
======================================
'''
class Widget:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Button(Widget):
    def __init__(self, x, y, label):
        super().__init__(x, y)
        self.label = label

btn = Button(100, 200, "OK")
print(btn.x, btn.y, btn.label)  # 100 200 OK

'''
======================================
7. Модифицируй Button, чтобы не вызывать super() вовсе.
Что произойдёт? Проверь через print(btn.__dict__).

появится в консоли только {'label': 'OK'}
связано это с тем, что мы не вызываем родительский инит 
а только init дочернего класса и переменные атрибуты x/y просто не записываются
======================================
'''
class Widget:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Button(Widget):
    def __init__(self, x, y, label):
        # super().__init__(x, y)
        self.label = label

btn = Button(100, 200, "OK")
print(btn.__dict__)

'''
======================================
8. Создай классы:
Logger — метод log(self, msg) просто печатает сообщение;
HTMLLogger(Logger) — переопредели метод log.
logger = HTMLLogger()
logger.log("Login successful")

Ожидаемый вывод (обрати внимание что выводится 2 строки:
одна из log класса Logger, другая из log класса HTMLLogger):
[LOG] Login successful
<p>Login successful</p>
======================================
'''
class Logger:
    def log(self, msg):
        print(f'[LOG] {msg}')

class HTMLLogger(Logger):
    def log(self, msg):
        super().log(msg)
        print(f"<p>{msg}</p>")

logger = HTMLLogger()
logger.log("Login successful123123123")
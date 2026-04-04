'''
------------------------------------------------------------------------------------------------------------------------
                                         Наследование класса
------------------------------------------------------------------------------------------------------------------------
'''

"""
На основе примера с автотестами для UI
"""

class BasePage: # - класс с общими методами для всех остальных страниц
    def open(self, url: str): # - метод, который позволяет открыть текущую страницу
        print(f'Открываем страницу {url}')
    def click(self, element_name): # - метод для клика по какому-либо элементу на странице
        print(f'Клик по элементу {element_name}')


class LoginPage(BasePage): # - класс отдельно для страницы логина. Наследует от class BasePage. В этом классе уже имеем оба метода из класса, от которого мы наследуем
    def login(self, username: str, password: str):
        print(f'Вход в аккаунт:\nЛогин: {username}\nПароль: {password}')

    def click(self, element_name: str): # - переопределили метод, который был наследован у главного класса, чтобы он работал по-другому для
        print(f'Клик по элементу на странице Входа {element_name}')


class CartPage(BasePage):
    def checkout(self):
        print('Оформление заказа')

login_page = LoginPage() # - создали экземпляр класса LoginPage
login_page.open('google.com') # - можем все равно использовать метода из class BasePage, от которого наследовали
login_page.click('log in') # - можем все равно использовать метода из class BasePage, от которого наследовали
login_page.login('username', 'password') # - отдельный метод который есть в классе class LoginPage для логина
print()
cart_page = CartPage()
cart_page.open('/cart')
cart_page.checkout()


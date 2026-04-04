'''
------------------------------------------------------------------------------------------------------------------------
                                    Обработка исключений через тег вызовов
------------------------------------------------------------------------------------------------------------------------
'''

'''
Базовый пример обработки исключения внутри класса
'''
# class Calculator:
#     def devide(self, a, b):
#         try:
#             return a / b
#         except ZeroDivisionError:
#             print('Ошибка деления на ноль')
#             return None
#
# calc = Calculator()
# print("Начинаем вычисление")
# res = calc.devide(10, 0)
# print(f'Результат: {res}')

'''
Пример с цепочкой вызовов
'''
# class APIClient: # - имитация сервиса, который сделали разработчики
#     def get_user(self, iser_id):
#         raise ConnectionError('Сервер недоступен')
#
# class UserService: # - АПИ класс или клиент, который обращается к сервису (обертка, через которую мы обращаемся к нашему сервису)
#     def __init__(self):
#         self.client = APIClient()
#     def get_user_info(self, user_id):
#         return self.client.get_user(user_id)
#
# class TestUserAPI: # - сам тест
#     def test_get_user(self):
#         client = UserService()
#         try:
#             client.get_user_info(1)
#         except ConnectionError as e:
#             print(f'Ошибка подключения: {e}')
#             assert False, "API не отвечает"
#
# TestUserAPI().test_get_user()

'''
Пример с базовым классом
'''
class BaseAPIClient:
    def request(self, endpoint):
        try:
            return self._send(endpoint)
        except Exception as e:
            print(f"Лог ошибки: {e}")
            raise
    def _send(self, endpoint):
        raise NotImplementedError

class ProductClient(BaseAPIClient):
    def _send(self, endpoint):
        raise TimeoutError('Превышено время ожидания')

client = ProductClient()
client.request('/product')


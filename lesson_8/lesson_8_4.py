'''
Декораторы Python
'''
# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Call function: {func.__name__}")
#         result = func(*args, **kwargs)
#         print(f"Finished: {func.__name__}")
#         return result
#     return wrapper
# @logger
# def test_example():
#     print('Выполняется текст')
# test_example()
'''
Декоратор из класса
Когда требуется сложные логические уровни логирования
'''
class Logger:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print(f"Call function: {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f"Finished: {self.func.__name__}")
        return result
@Logger
def test_example():
    print('Выполняется текст')
test_example()


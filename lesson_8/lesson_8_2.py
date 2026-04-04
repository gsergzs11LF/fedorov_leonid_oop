'''
Как создать свое пользовательское исключение
'''
class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f'Print: {data}')

    def send_data(self, data):
        if not self.send_to_print(data):
            raise PrintError('Принтер не отвечает', code=503)

    def send_to_print(self, data):
        return False

class PrintError(Exception):
    '''Ошибка печати'''
    def __init__(self, message, code=None):
        self.message = message
        self.code = code
    def __str__(self):
        return f'[Ошибка: {self.code}] {self.message}' if self.code else self.message



p = PrintData()
try:
    p.send_data('Отчет')
except PrintError as e:
    print(f"Ошибка печати: {e}")
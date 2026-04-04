'''
Контекстный менеджер
'''

# with open('data.txt') as f:
#     for line in f:
#         print(line, end='')

import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def __enter__(self): # - отрабатывает когда входим в класс при помощи контекстного менеджера with
        self.session = requests.Session()
        print('Подключение к API')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        print('Соединение закрыто')
        return False

    def get(self, path, **kwargs):
        url = f"{self.base_url}{path}"
        return self.session.get(url, **kwargs)

def test_get_users():
    with APIClient('http://reqres.in') as s:
        resp = s.get('/api/users?page=1')
        print(resp.json())
        assert resp.status_code == 200
test_get_users()

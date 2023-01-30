import requests

# Пользователи

# response = requests.post('http://127.0.0.1:5000/users/',
#                          json={'name': 'Alex1',
#                                'email': 'alex1@mail.ru',
#                                'password': '12345'})
# response = requests.get('http://127.0.0.1:5000/users/4')


# Объявления

# response = requests.post('http://127.0.0.1:5000/articles/',
#                          json={'title': 'Объявление 2',
#                                'description': 'Описание 2',
#                                'id_user': 2})

# response = requests.patch('http://127.0.0.1:5000/articles/',
#                           json={'id': 4,
#                                 'description': 'Новое описание2',
#                                 'id_user': 1})

response = requests.get('http://127.0.0.1:5000/articles/4')

# response = requests.delete('http://127.0.0.1:5000/articles/', json={'id': 4, 'id_user': 2})

print(response.json())

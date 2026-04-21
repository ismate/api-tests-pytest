#                                                                                   ======== ПЕРЕМЕННЫЕ/ТИПЫ =========

# import requests

# my_name = 'Oleg'
# my_age = 22
# hobbies = ['Programming','Basketball','Cars']
# print(my_name)
# print(my_age)
# print(hobbies)
# print(hobbies[0])
#                                                                                ==========     STATUS_CODES   ===========
# status_code = 200
# if status_code == 200: 
#     print('OK')
# elif status_code == 404:
#     print('Not found')
# elif status_code == 500:
#     print('Server error')
# else :
#     print('unknown status')

# status_codes = [200, 404, 500, 200, 403]
# def check_status(status): 
#         if status == 200:
#             print('OK')
#         elif status == 404:
#             print('Not Found')
#         elif status == 500:
#             print('Server error')
#         else:
#             print('Unknown')
# for code in status_codes:
#      check_status(code)

# users = [
#     {"name": "Анна", "age": 25, "city": "Москва"},
#     {"name": "Иван", "age": 30, "city": "СПб"},
#     {"name": "Олег", "age": 22, "city": "Москва"}
# ]
# for user in users:
#     print(f"Имя: {user['name']}, Возраст: {user['age']}, Город: {user['city']}")

                                                                                        #==========     ASSERTS    ============
# import requests

# url = "https://jsonplaceholder.typicode.com/posts/"
# response = requests.get(url)
# data = response.json()

# print('Кол-во постов:', len(data))
# print('Заголовок первого поста:', data[0]['title'])

# import requests

# url = "https://jsonplaceholder.typicode.com/posts"
# response = requests.get(url)

# # 1. Проверка статуса
# assert response.status_code == 200, f"Ошибка: статус {response.status_code}"

# posts = response.json()

# # 2. Проверка, что ответ — это список
# assert isinstance(posts, list), f"Ошибка: ожидали список, получили {type(posts)}"

# # 3. Проверка, что список не пустой
# assert len(posts) > 0, "Список постов пуст"

# # 4. Проверка, что у первого элемента есть нужные поля
# first_post = posts[1]
# assert "id" in first_post, "Нет поля id"
# assert "title" in first_post, "Нет поля title"
# assert "body" in first_post, "Нет поля body"

# print("✅ Все тесты пройдены")
# print(f"Количество постов: {len(posts)}")
# print(f"Заголовок первого поста: {posts[0]['title']}")

                                                                                        
# import requests
# url = "https://jsonplaceholder.typicode.com/posts/"
# response = requests.get(url)
# posts = response.json()

# assert response.status_code == 200, f'Ошибка: статус {response.status_code}'

# assert isinstance(posts,list), f'Ошибка : ожидали список, получили {type(posts)}'

# assert len(posts) > 0, f'Ошибка: список пустой'
# second_post = posts[1]

# assert 'id' in second_post, f'Нет поля id'
# assert 'title' in second_post, f'Нет поля title'
# assert 'body' in second_post, f'Нет поля body'

# print(f'Заголовок первого поста:{posts[0]["title"]} ')


#                                                                     ===================  POST - REQUESTS =======================
# import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# # Данные для нового поста
# new_post = {
#     "title": "Мой тестовый пост",
#     "body": "Учусь писать POST-запросы на Python",
#     "userId": 1
# }

# # Отправляем POST-запрос
# response = requests.post(url, json=new_post)

# # Проверка статуса (должен быть 201 Created)
# assert response.status_code == 201, f"Ошибка: статус {response.status_code}"

# # Получаем созданный пост из ответа
# created_post = response.json()

# # Проверяем, что пришёл ответ с id
# assert "id" in created_post, "Нет поля id в ответе"
# assert created_post["title"] == new_post["title"], "Заголовок не совпадает"

# print(f"✅ Пост создан! ID: {created_post['id']}")
# print(f"Заголовок: {created_post['title']}")
# print(f"Тело: {created_post['body']}")

import requests 
url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "Быстрый тест",
    "body": "Проверка связи",
    "userId": 1
}
response = requests.post(url, json = new_post)
assert response.status_code == 201,f'Ошибка: статус: {response.status_code}'

created_post = response.json()

assert "id" in created_post, f'Нет id в созданном посте'
print(f"id нового поста: {created_post['id']}")

assert created_post["title"] == new_post["title"], "заголовок не совпадает"

# import requests

# my_name = 'Oleg'
# my_age = 22
# hobbies = ['Programming','Basketball','Cars']
# print(my_name)
# print(my_age)
# print(hobbies)
# print(hobbies[0])

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


# import requests

# url = "https://jsonplaceholder.typicode.com/posts/"
# response = requests.get(url)
# data = response.json()

# print('Кол-во постов:', len(data))
# print('Заголовок первого поста:', data[0]['title'])


# status = response["status"]
# users = response["data"]["users"]

# if status == 200:
#     print("OK")
# else:
#     print("ERROR")


# def find_duplicates(users):
#     ids = [user["id"] for user in users]
#     return len(ids) != len(set(ids))


# if find_duplicates(users):
#     print("Есть дубликаты ID")
# else:
#     print("Дубликатов нет")


# admin_count = sum(1 for user in users if user["username"] == "admin")

# if admin_count == 2:
#     print("admin встречается 2 раза")
# else:
#     print("другое количество admin")


#     users = response["data"]["users"]["name"] for user in users 
#     ids = response["data"]["users"] for user in users 
#     if len("ids") != len(set("ids")): 
#         print("есть дубликаты id ") 
#         else: print("дубликатов нет")


# result = []

# for user in users:
#     if user["name"] == "admin":
#         result.append(user["name"])


# Если хотим найти все четные числа больше 10 в списке, то можно использовать генератор списков:
# nums = [3, 7, 10, 15, 22, 5, 8]

# result = [x for x in nums if x % 2 == 0 and x > 10]

# print(result)
# [<результат_для_каждого_элемента> for <элемент> in <список>]

# Сделаем генератор списков, который преобразует все слова в верхний регистр, но только для слов длиной 5 и более символов:
# words = ["apple", "banana", "kiwi", "strawberry", "pear"]

# result = [x.upper() for x in words if len(x) >= 5]
# print(result)

# Умножим все числа, которые делятся на 3, на 2:
# nums = [12, 5, 18, 7, 21, 10, 3, 30]
# result = [x * 2 for x in nums if x % 3 == 0]
# print(result)


# Верним имена всех пользователей, которые старше 18 лет:
# users = [
#     {"name": "Alex", "age": 25},
#     {"name": "Bob", "age": 17},
#     {"name": "John", "age": 30},
#     {"name": "Kate", "age": 16},
# ]

# result = [user["name"] for user in users if user["age"] >= 18]
# print(result)

# [ЧТО_вернуть for ЭЛЕМЕНТ in СПИСОК if УСЛОВИЕ]

# верним id всех пользователей, у которых статус "active":
# response = [
#     {"id": 1, "status": "active"},
#     {"id": 2, "status": "inactive"},
#     {"id": 3, "status": "active"},
#     {"id": 4, "status": "inactive"}
# ]

# activeIds = [user["id"] for user in response if user["status"] == "active"]
# print(activeIds)

# response = [
#     {"id": 1, "status": "active", "age": 25},
#     {"id": 2, "status": "inactive", "age": 17},
#     {"id": 3, "status": "active", "age": 19},
#     {"id": 4, "status": "active", "age": 16}
# ]
# result = [user["id"]for user in response if user["status"] == "active" and user["age"] >= 18]
# print(result)

    # Проверки : статус код 200, тип данных, наличие данных, наличие ключа id в каждом пользователе

# import requests

# def test_users_api():
#     response = requests.get("https://jsonplaceholder.typicode.com/users")
#     data = response.json()

#     assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
#     assert isinstance(data,list), "Response is not a list"
#     assert len(data) > 0, "No users found in response"
    
#     for user in data:
#         assert "id" in user, "User does not have 'id'"


# Негативный тест: проверим, что при запросе несуществующего эндпоинта возвращается статус код 404
# import requests

# def test_wrong_endpoint():
#     response = requests.get("https://jsonplaceholder.typicode.com/userzzz")

#     print("STATUS:", response.status_code)

#     assert response.status_code == 404



# import requests

# def test_first_user_structure():
#     response = requests.get("https://jsonplaceholder.typicode.com/users")
#     data = response.json()

#     assert response.status_code == 200, f"статус код: {response.status_code}"
#     assert isinstance(data,list), "Ответ не является списком"
#     assert len(data) > 0, "Список не пустой"
#     first_user = data[0]

#     assert "id" in first_user, "Нет ключа id"
#     assert "name" in first_user, "Нет ключа name"
#     assert "email" in first_user, "Нет ключа email"
        
# Проверка наличия вложенных полей в первом пользователе, например, "address" с полями "city" и "geo", а в "geo" должны быть "lat" и "lng":


# "user": {
#     "address": {
#         "city": "...",
#         "geo": {
#             "lat": "...",
#             "lng": "..."
#         }
#     }
# }

# import requests

# def test_user_nested_fields():
#     response = requests.get("https://jsonplaceholder.typicode.com/users")
#     data = response.json()

#     assert response.status_code == 200, f"статус код: {response.status_code}"
    
#     first_user = data[0]

#     address = first_user["address"]
#     assert "address" in first_user, "Нет ключа address"
#     assert "city" in address, "Нет ключа city в address"
#     assert "geo" in address, "Нет ключа geo в address"

#     geo = address["geo"]
#     assert "lat" in geo, "Нет ключа lat в geo"
#     assert "lng" in geo, "Нет ключа lng в geo"

# import requests

# def test_user_types():
#     response = requests.get("https://jsonplaceholder.typicode.com/users")
#     data = response.json()

#     first_user = data[0]

#     assert isinstance(first_user["id"], int), "id не является числом"
#     assert isinstance(first_user["name"], str), "name не является строкой"
#     assert isinstance(first_user["email"], str), "email не является строкой"
#     assert isinstance(first_user["address"], dict), "address не является словарем"


# Проверка наличия символа "@" в Email , есть имя и id
# import requests


# def test_user_values():
#     response = requests.get("https://jsonplaceholder.typicode.com/users")
#     data = response.json()

#     first_user = data[0]

#     assert "@" in first_user["email"], "email не содержит символ @"
#     assert "id" in first_user, "here"
#     assert first_user["id"] > 0, "id должен быть положительным числом"
#     assert "name" in first_user and len(first_user["name"]) > 0, "name не должен быть пустой строкой"


# Проверка всех пользователей на наличие id, email с символом "@", и имени не пустой строкой
# import requests

# def test_all_users_have_id():

#     response = requests.get("https://jsonplaceholder.typicode.com/users")
#     data = response.json()

#     for user in data:
#         assert "id" in user, f"У пользователя {user} нет ключа id"
#         assert user["id"] > 0, f"id пользователя {user['id']} не является положительным числом"
#         assert "email" in user, f"У пользователя {user} нет ключа email"
#         assert "@" in user["email"], f"email пользователя {user['email']} не содержит символ @"
#         assert "name" in user, f"У пользователя {user} нет ключа name"
#         assert len(user["name"]) > 0, f"name пользователя {user['name']} не должен быть пустой строкой"




                                    # --------------------------PYTEST------------
# import pytest

# @pytest.mark.parametrize("переменная", [значения])
# def test_func(переменная):
#     ...


# Проверка, что user_id является положительным числом, используя параметризацию в pytest:
# import pytest

# @pytest.mark.parametrize("user_id", [1, 5, 10, 100, -1])

# def test_user_id_positive(user_id):
#     assert user_id > 0, f"user_id {user_id} должен быть положительным числом"


# import pytest

# Emails = ["test@mail.com",
#     "user@gmail.com",
#     "wrongemail",
#     "admin@yandex.ru"
#     ]

# @pytest.mark.parametrize("email", Emails)
# def test_email_format(email):
#     assert "@" in email, f"email {email} не содержит символ @"

#     Ты прошёл:

# list comprehension
# работа со списками и словарями
# понимание JSON структуры
# requests (GET)
# pytest + assert
# негативные кейсы
# parametrize

# Это уже цельный блок навыков.



# import requests
# import pytest

# payload = {
#     "name": "Oleg",
#     "email": "wrongemail"
# }

# def test_wrong_email():

#     response = requests.post("https://jsonplaceholder.typicode.com/users", json=payload)
#     data = response.json()

#     assert response.status_code == 201, f"Unexpected status code:{response.status_code}"
#     assert "@" not in payload["email"], "ЕМЭИЛ НЕ СОДЕРЖИТ СИМВОЛ @"

# Проверка создания дубликата пользователя с помощью POST запроса, и что при этом возвращается статус код 400 и сообщение об ошибке "Email already exists":
# import requests
# import pytest

# # def test_get_users():
# #     url = "http://127.0.0.1:8000/users"
# #     response = requests.get(url)
# #     data = response.json()
# #     assert response.status_code == 200, f"code = {response.status_code}"
# #     assert isinstance(data, list), "Ответ не список"
# #     assert len(data) > 0, "список не пустой" 


# def test_create_user_deplicate():
#     url="http://127.0.0.1:8000/users"

#     payload = {
#         "name" : "Oleg",
#         "email" : "Oleg@example.com"
#     }
#     payload2 = {
#         "name" : "vaskka",
#         "email" : "vaskka@example.com"
#     }

#     response1 = requests.post(url, json=payload)
#     response2 = requests.post(url, json=payload2)
#     data1 = response1.json()
#     data2 = response2.json()

#     # response2 = requests.post(url, json=payload)
#     # data2 = response2.json()

#     # assert response2.status_code == 400, f"code = {response2.status_code}"
#     assert response1.status_code == 201, f"code = {response1.status_code}"
#     assert response2.status_code == 201, f"code = {response2.status_code}"
#     # assert data2["detail"] == "Email already exists"

# import requests
# import pytest

# def test_creat_multiplye_users():
#     url = "http://127.0.0.1:8000/users"

#     users = [
#         {"name": "Oleg","email": "oleg@example.com"},
#         {"name": "Vaskka","email": "vaskka@example.com"},
#         {"name": "Olga","email": "Olga@example.com"},
#         {"name": "Maria","email": "Maria@example.com"}
#     ]

#     for user in users :
#         response = requests.post(url, json=user)
#         assert response.status_code == 201, f"code = {response.status_code}"

#         response_get = requests.get(url)
#         data = response_get.json()

#         assert response_get.status_code == 200, f"code = {response_get.status_code}"
#         assert isinstance(data, list), "Ответ не список"
#         assert len(data) >= 3, "список пустой"


# import requests

# def test_unexisting_user():
#     url = "http://127.0.0.1:8000/users/999"
#     response = requests.get(url)

#     print("STATUS:", response.status_code)
#     print("TEXT:", response.text)

#     assert response.status_code == 404, f"code = {response.status_code}"

# ------------------------ FIXTURE ------------------------ Аргументы перед тестом
# import requests
# import pytest

# @pytest.fixture()
# def base_url():
#     return "http://127.0.0.1:8000"

# def test_unexisting_user(base_url):
#     response = requests.get(f"{base_url}/users/999")

#     print("STATUS:", response.status_code)
#     print("TEXT:", response.text)

#     assert response.status_code == 404

# import random

# import requests
# import pytest

# @pytest.fixture()
# def base_url():
#     return "http://127.0.0.1:8000"

# @pytest.fixture()
# def create_user(base_url):
#     payload = {
#         "name": "Oleg",
#         "email": f"oleg_{random.randint(1,1000)}@example.com"
        
#     }
#     response = requests.post(f"{base_url}/users", json=payload)

#     assert response.status_code == 201, f"code = {response.status_code}"

#     user_data = response.json()
#     yield user_data

#     # teardown - удалим созданного пользователя после теста

#     requests.delete(f"{base_url}/users/{user_data['id']}")





        #    ---------------------------СОЗДАНИЕ,ОБНОВЛЕНИЕ И ПРОВЕРКА НОВОГО ПОЛЬЗОВАТЕЛЯ---------------------
# import random
# import requests
# import pytest

# pytest.fixture()
# def base_url():
#     return "http://127.0.0.1:8000"

# pytest.fixture()
# def user_payload():
#     return {
#         "name": "Oleg",
#         "email" : f"Oleg_{random.randint(1,1000)}@gmail.com"}

# pytest.fixture()
# def create_user(base_url, user_payload):
#     response = requests.post(f"{base_url}/users", json=user_payload)

#     assert response.status_code == 201
#     user_data = response.json()
#     yield user_data
    
#     delete_response = requests.delete(f"{base_url}/users/{user_data['id']}")


# def test_update_user(base_url,create_user):
#     user_id = create_user["id"]

#     update_payload = {
#         "name" : "updated_name"
#     }
#     patch_response = requests.patch(f"{base_url}/users/{user_id}", json=update_payload)
#     assert patch_response.status_code == 200
#     get_response = requests.get(f"{base_url}/users/{user_id}")
#     data = get_response.json()
#     assert get_response.status_code == 200, f"Code :{response.status_code}"
#     assert data["id"] == user_id
#     assert data["name"] == update_payload["name"]
#     assert data["email"] == create_user["email"]


import random
import requests
import pytest

@pytest.fixture()
def base_url():
    return "http://127.0.0.1:8000"

@pytest.fixture()
def user_payload():
    return {
        "name": "Oleg",
        "email" : f"Oleg_{random.randint(1,1000)}@gmail.com"}

@pytest.fixture()
def create_user(base_url, user_payload):
    response = requests.post(f"{base_url}/users", json=user_payload)

    assert response.status_code == 201
    user_data = response.json()
    yield user_data
    
    delete_response = requests.delete(f"{base_url}/users/{user_data['id']}")

# def test_unexisting_user(base_url):
#     update_payload = {
#         "name": "Ivan"
#     }
#     patch_response = requests.patch(f"{base_url}/users/999", json=update_payload)
#     assert patch_response.status_code == 404,f"{patch_response.status_code}"
#     data = patch_response.json()
#     assert "detail" in data

    # def test_invalid_user_data(base_url,create_user):
    #     invalid_payload = {
    #         "name":"",
    #         "email": ""
    #     }


    #     user_id = create_user["id"]
    #     patch_response = requests.patch(f"{base_url}/users/{user_id}",json=invalid_payload)
    #     assert patch_response.status_code in (400,422)

    #     get_response = requests.get(f"{base_url}/users/{user_id}")
    #     data = get_response.json()
    #     assert data["name"] == create_user["name"]
    #     assert data["email"] == create_user["email"]

def test_user_with_headers(base_url,create_user):
    user_id = create_user["id"]

    headers = {
            "Authorization" : "Bearer testtoken123"
        }
    get_response = requests.get(f"{base_url}/users/{user_id}", headers=headers)
    assert get_response.status_code == 200,f"Code is {get_response.status_code}"
    assert get_response.json()["id"] == user_id
        
def test_invalid_headers_user(base_url,create_user):
    user_id = create_user["id"]
    headers ={
            "Authorization" : ""
        }
    get_response = requests.get(f"{base_url}/users/{user_id}", headers=headers)
    assert get_response.status_code in(401, 403)

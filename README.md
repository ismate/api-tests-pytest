# API Tests with Pytest + Requests

Проект по автоматизации API-тестов на Python.

## Стек

- Python
- pytest
- requests
- pydantic
- Faker
- FastAPI

## Что покрыто тестами

- GET пользователя с валидной авторизацией
- PATCH пользователя
- Проверка 401 при отсутствии/невалидном токене
- Проверка 404 для несуществующего пользователя
- Проверка 422 при невалидных данных
- Проверка, что данные не изменяются после неуспешного PATCH
- Schema validation через pydantic

## Структура проекта

```text
api-tests-pytest/
├── api/
│   └── users_api.py
├── schemas/
│   └── user_schema.py
├── tests/
│   └── test_users.py
├── conftest.py
├── main_fastapi.py
├── requirements.txt
└── README.md
```
## Запуск тестов
```bash
python -m pytest -v -s
```
## Запуск сервера
```bash
python -m uvicorn main_fastapi:app --reload

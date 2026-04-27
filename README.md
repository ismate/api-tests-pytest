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
```
## Подходы

- **Fixtures (pytest)** — создание и удаление тестовых данных через `yield`
- **Parametrize** — покрытие нескольких сценариев (payload, headers) в одном тесте
- **Schema validation (pydantic)** — проверка структуры и типов данных ответа API

## Проверяемые статус-коды
- 200 OK
- 201 Created
- 401 Unauthorized
- 404 Not Found
- 422 Unprocessable Entity

## QA Портфолио

- [QA Portfolio](https://github.com/ismate/qa-portfolio)

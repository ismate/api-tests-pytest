# API Tests with Pytest + Requests
![CI](https://github.com/ismate/api-tests-pytest/actions/workflows/python-tests.yml/badge.svg)
Проект автоматизации API-тестов на Python с использованием pytest, requests и pydantic.

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
- Проверка списка пользователей (GET /users)

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
## Запуск сервера
```bash
python -m uvicorn main_fastapi:app --reload
```
## Запуск тестов
```bash
python -m pytest -v -s
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
- 
## Особенности

- Разделение API-слоя и тестов
- Использование fixtures для управления тестовыми данными
- Проверка состояния данных после API-операций
- Schema validation (pydantic)
- Data-driven тестирование с помощью parametrize

## QA Портфолио

- [QA Portfolio](https://github.com/ismate/qa-portfolio)

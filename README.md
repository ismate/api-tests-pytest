# API тесты (pytest)

## Стек
- Python
- pytest
- requests
- FastAPI (локальный сервер)

## Что покрыто
- GET /users
- POST /users
- PATCH /users
- DELETE /users
- 404 (несуществующий пользователь)
- валидация (невалидные данные)
- авторизация (Bearer token)

## Структура проекта
- api/ — работа с API
- tests/ — тесты
- data/ — тестовые данные
- conftest.py — фикстуры
- main_fastapi.py — тестовый сервер

## Запуск тестов
```bash
pytest -v

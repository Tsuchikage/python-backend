# Homework 1

## Task
- Создать "Hello world" на понравившемся фреймворке
- Создать несколько entry point: с path параметром, query параметром и request body
- Настроить линтеры, форматтеры
- Написать комментарии для всех функций и entry point

## Run
```bash
pip install poetry
poetry install
```

```bash
cd .\Homework_1\
poetry run uvicorn app:app --port 8000
```

## Linter and Code Formatter
```bash
poetry run pylint .\Homework_1\app.py
poetry run pylint .\Homework_1\routers.py
poetry run black .\Homework_1\app.py .\Homework_1\routers.py
```

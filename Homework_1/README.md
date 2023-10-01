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

## Pre-Commit Integration
Для обеспечения качества кода, используется Pre-Commit. Он автоматизирует процесс проверки и форматирования кода перед коммитом.

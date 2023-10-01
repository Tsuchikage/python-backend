# Python Backend Course

## Topics
- Python Web Technologies
- Testing
- Communication Technologies
- Microservices
- Databases
- Message Brokers
- CI/CD


# Homework 1

## Task
- Создать "Hello world" на понравившемся фреймворке
- Создать несколько entry point: с path параметром, query параметром и request body
- Настроить линтеры, форматтеры
- Написать комментарии для всех функций и entry point

## Run
```bash
pip install -r requirements.txt
```

```bash
uvicorn server.src.app:app --reload
```

## Pre-Commit Integration
Для обеспечения качества кода, используется Pre-Commit. Он автоматизирует процесс проверки и форматирования кода перед коммитом.

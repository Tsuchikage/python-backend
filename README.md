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
docker-compose up db
```

```bash
uvicorn server.src.app:app --reload
```

## Pre-Commit Integration
Для обеспечения качества кода, используется Pre-Commit. Он автоматизирует процесс проверки и форматирования кода перед коммитом.


# Homework 2

## Task
- Придумать бизнес сценарий для вашего веб приложения и описать его в PR
- Написать Endpoint’ы для бизнес сценариев и вынести логику работы в отдельные модули\функции
- Бизнес логика должна быть достаточно сложной, чтобы описать её в как минимум трех функциях\методах
- Разработать три модульных теста для каждой функции/метода
- Разработать три интеграционных теста
- Задокументировать, как автоматически выполнять тесты

## Description
Проект **To Do List** представляет собой приложение, с помощью которого можно составлять список задач.
- добавление задач в список
- удаление задач из списка
- редактирование задачи
- просмотр всех созданных задач

## Run Tests
```bash
python -m pytest
```


# Homework 3

## Task
- Создать Python проект и определить несколько микросервисов
- Для каждого микросервиса определите API, используя gRPC или HTTP, для взаимодействия между сервисами.
- Покрыть функционал тестами


## Description
Проект представляет собой приложение из двух микросервисов.
- Inventory - создание/редактирование/просмотр товара
- Payment - создание заказа по id и quantity (количеству) товара

## Run
```bash
docker-compose up
```
```bash
uvicorn server.inventory.main:app --reload
```
```bash
uvicorn server.payment.main:app --reload --port=8001
```
```bash
python -m pytest
```
Тесты создают товар и заказ, и получают об этом информацию.


# Homework 4

## Task
- Реализовать простую логику с использованием celery и rabbitmq

## Run
```bash
docker-compose up
```

## Description
- Отправить несколько запросов. Результаты отобразятся в консоли.
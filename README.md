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
- Create a "Hello World" using a framework of your choice
- Create several entry points: with a path parameter, a query parameter, and a request body
- Configure linters and formatters
- Write comments for all functions and entry points

## Run
```bash
pip install -r requirements.txt
docker-compose up db
```

```bash
uvicorn server.src.app:app --reload
```

## Pre-Commit Integration
To ensure code quality, Pre-Commit is used. It automates the process of checking and formatting code before committing.


# Homework 2

## Task
- Come up with a business scenario for your web application and describe it in a PR
- Write endpoints for the business scenarios and move the logic into separate modules/functions
- The business logic must be complex enough to be described in at least three functions/methods
- Develop three unit tests for each function/method
- Develop three integration tests
- Document how to run the tests automatically

## Description
The **To Do List** project is an application that allows you to create a task list:
- Add tasks to the list
- Remove tasks from the list
- Edit tasks
- View all created tasks

## Run Tests
```bash
python -m pytest
```


# Homework 3

## Task
- Create a Python project and define several microservices
- For each microservice, define an API using gRPC or HTTP for interservice communication
- Cover the functionality with tests

## Description
The project is an application consisting of two microservices:
- **Inventory** – creation/editing/viewing of products
- **Payment** – creation of an order by product ID and quantity

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
The tests create a product and an order, then retrieve information about them.


# Homework 4

## Task
- Implement simple logic using Celery and RabbitMQ

## Run
```bash
docker-compose up
```

## Description
- Send several requests. The results will be displayed in the console.

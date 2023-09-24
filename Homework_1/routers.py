from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/")
async def hello_world():
    """
    :return: Возвращает "Hello, World!".
    """
    return {"message": "Hello, World!"}


@router.get("/greet/{name}")
async def greet_name(name: str):
    """
    Выполняет приветствие с именем.
    :param name: Имя
    :return: Возвращает "Hello, {name}!".
    """
    return {"message": f"Hello, {name}!"}


@router.get("/double")
async def double_query_param(number: int = Query(..., description="Enter a number")):
    """
    Выполняет увдоение числа из query параметра.
    :param number: Число
    :return: Возвращает удвоенное число.
    """
    return {"result": number * 2}


@router.post("/greet/")
async def greet_request_body(data: dict):
    """
    Выполняет приветствие с использованием данных из JSON-тела запроса.
    :param data: JSON-тело запроса с полем 'name'
    :return: Возвращает JSON-ответ с приветствием.
    """
    return {"message": f"Hello, {data['name']}!"}
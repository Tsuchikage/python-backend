from time import sleep
from celery import Celery
from celery.utils.log import get_task_logger

celery = Celery('tasks', broker='amqp://guest:guest@127.0.0.1:5672//')
celery_log = get_task_logger(__name__)


@celery.task
def create_order(product_name, quantity):
    # 5 секунд на 1 заказ
    complete_time_per_item = 5

    # Постоянно увеличивается в зависимости от количества заказываемых изделий
    sleep(complete_time_per_item * quantity)
    celery_log.info(f"Order Complete!")
    return {"message": f"Order created!",
            "product_name": product_name,
            "order_quantity": quantity}

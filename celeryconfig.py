from celery import Celery
import os

app = Celery('celery_app',
             broker='amqp://guest:guest@rabbitmq:5672/vhost',
             include=['task'])

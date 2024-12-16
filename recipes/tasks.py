from celery import shared_task
from celery.schedules import crontab
from celery import Celery
import datetime

from celery import shared_task

@shared_task
def task1():
    # Ваш код для первой задачи
    print("Выполняется задача 1")
    return "Задача 1 выполнена"

@shared_task
def task2():
    # Ваш код для второй задачи
    print("Выполняется задача 2")
    return "Задача 2 выполнена"
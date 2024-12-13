from celery import shared_task
from celery.schedules import crontab
from celery import Celery
import datetime

app = Celery('recept')

@shared_task
def print_current_time():
    """Печатает текущее время в консоль."""
    now = datetime.datetime.now()
    print(f'Current time is: {now.strftime("%Y-%m-%d %H:%M:%S")}')

@shared_task
def print_hello_world():
    """Печатает сообщение 'Hello, World!' в консоль."""
    print("Hello, World!")

# Настройка периодических задач
app.conf.beat_schedule = {
    'print-time-every-minute': {
        'task': 'your_app_name.tasks.print_current_time',  # Замените на имя вашего приложения
        'schedule': crontab(minute='*'),  # Каждый минуту
    },
    'print-hello-every-15-minutes': {
        'task': 'your_app_name.tasks.print_hello_world',  # Замените на имя вашего приложения
        'schedule': crontab(minute='*/15'),  # Каждые 15 минут
    },
}

# Настройка брокера сообщений, если это не сделано в другом месте
app.conf.broker_url = 'redis://localhost:6379/0'  # Укажите ваш Redis URL

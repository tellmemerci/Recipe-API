import os
from celery import Celery

# установите модуль настроек Django по умолчанию для программы 'celery'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recept.settings')

app = Celery('recept')

# Загрузка конфигурации из объекта настроек Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение и регистрация задач из всех приложений Django
app.autodiscover_tasks()
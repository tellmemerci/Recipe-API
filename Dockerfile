# Основа образа - Python 3.12
FROM python:3.12-slim

# Обновляем pip
RUN pip install --upgrade pip

# Установка необходимых пакетов
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Создание директории для проекта
WORKDIR /app

# Копирование файлов проекта в контейнер
COPY . /app

# Запуск Django сервера с миграциями, если они нужны
CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

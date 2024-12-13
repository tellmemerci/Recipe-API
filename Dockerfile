# Указываем базовый образ
FROM python:3.12-slim

# Условия работы
WORKDIR /app

# Обновляем pip
RUN pip install --upgrade pip

# Копируем файл зависимостей
COPY requirements.txt ./

# Устанавливаем необходимые пакеты
RUN pip install -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . .

# Запуск приложения Django
CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

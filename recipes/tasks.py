from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
from .models import Recipe
from django.db import models
@shared_task
def task1():
    """Отправка тестового письма через Яндекс"""
    subject = 'Тестовое письмо от Django Celery'
    message = f'''
    Привет!
    Это тестовое письмо отправлено через Celery в {datetime.now().strftime("%H:%M:%S")}
    
    С уважением,
    Ваше приложение Recipes
    '''
    
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_ADMIN],  # или любой другой email
        fail_silently=False,
    )
    print(f"Задача 1: письмо отправлено на {settings.EMAIL_ADMIN}")
    return "Задача 1 выполнена - email отправлен"


@shared_task
def task2():
    """Отправка дайджеста популярных рецептов"""
    # Получаем 5 уникальных рецептов с подсчетом лайков
    popular_recipes = Recipe.objects.filter(
        is_public=True
    ).annotate(
        likes_count=models.Count('recipelike')
    ).order_by('-likes_count')[:5]

    subject = 'Популярные рецепты в нашей коллекции'
    message = 'Топ-5 рецептов по количеству лайков:\n\n'

    for recipe in popular_recipes:
        message += f'- {recipe.name} (Лайков: {recipe.likes_count})\n'
        if recipe.adversting_text:
            message += f'  Описание: {recipe.adversting_text[:100]}...\n'
        message += f'  Время приготовления: {recipe.time_of_cooking} минут\n'
        message += f'  Калории: {recipe.calories}\n\n'

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_ADMIN],
        fail_silently=False,
    )
    print(f"Задача 2: дайджест отправлен на {settings.EMAIL_ADMIN}")
    return "Задача 2 выполнена - дайджест отправлен"
from django.core.mail import send_mail
from recept import settings

def send_recipe_site_email(recipient_email):
    """Отправляет письмо о сайте рецептов."""

    subject = "Добро пожаловать на сайт рецептов!"
    message = "Это сайт с рецептами! Мы научим Вас готовить по возможности!"
    from_email = settings.DEFAULT_FROM_EMAIL  # Получение адреса отправителя из настроек
    recipient_list = [recipient_email]

    try:
        send_mail(subject, message, from_email, recipient_list)
        print("Письмо отправлено успешно!")
    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")
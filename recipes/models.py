from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    gender = models.CharField(max_length=20, choices=(('Мужской', 'Мужской'), ('Женский', 'Женский')),
                              default='Мужской', verbose_name='Пол')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    username = models.CharField(max_length=255, unique=True, verbose_name='Имя пользователя')
    email = models.EmailField(max_length=255, unique=True, verbose_name='Электронная почта')
    password = models.CharField(max_length=255, verbose_name='Пароль')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    role = models.CharField(max_length=50, default='Пользователь', verbose_name='Роль')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',
    )

    def __str__(self):
        return self.username

class Recipe(models.Model):
    name = models.CharField(max_length=500, verbose_name='Рецепты')
    photo_url = models.URLField(blank=True, verbose_name='Ссылка на главную фотографию ')
    calories = models.IntegerField(null=True, blank=True, verbose_name='калории')
    is_public = models.BooleanField(default=True, verbose_name='Публичность')
    status = models.CharField(max_length=50, default='На модерации', verbose_name='Статус')
    adversting_text = models.CharField(max_length=500, blank=True, verbose_name='Рекламирующий текст')
    time_of_cooking = models.IntegerField(verbose_name='Время приготовления')
    number_of_servings = models.IntegerField(verbose_name='Количество персон')
    status_site = models.CharField(max_length=50, blank=True, verbose_name='Статус на сайте')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')
    ingredient_name = models.CharField(max_length=500,  verbose_name='Название ингредиентов')
    quantity = models.CharField(max_length=500, verbose_name='Количество')
    measurement_name = models.CharField(max_length=500, verbose_name='Измерение')

    def __str__(self):
        return f"{self.ingredient_name} ({self.quantity})"

    class Meta:
        verbose_name = 'Ингредиент рецепта'
        verbose_name_plural = 'Ингредиенты рецептов'

class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')
    step_number = models.IntegerField(verbose_name='Номер шага')
    description = models.TextField(verbose_name='Описание')
    photo_url = models.URLField(blank=True, verbose_name='Ссылка на фото шага')

    def __str__(self):
        return f"Шаг {self.step_number}"

    class Meta:
        verbose_name = 'Шаг рецепта'
        verbose_name_plural = 'Шаги рецептов'

class RecipeLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Лайк на рецепт')

    class Meta:
        unique_together = ('user', 'recipe')
        verbose_name = 'Лайк рецепта'
        verbose_name_plural = 'Лайки рецептов'

class RecipeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')
    text = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=(('На модерации', 'На модерации'), ('Опубликован', 'Опубликован'),
                                                      ('Отклонят', 'Отклонят')),
                              default='На модерации', verbose_name='Статус комментария')
    text_of_moderation = models.CharField(max_length=500, blank=True, verbose_name='Ответ модератора')

    class Meta:
        verbose_name = 'Комментарий к рецепту'
        verbose_name_plural = 'Комментарии к рецептам'

class Calories(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='calories_info', verbose_name='Рецепт')
    protein = models.IntegerField(null=True, blank=True, verbose_name='Белки')
    fat = models.IntegerField(null=True, blank=True, verbose_name='Жиры')
    carbohydrates = models.IntegerField(null=True, blank=True, verbose_name='Углеводы')

    def __str__(self):
        return self.recipe.name

    class Meta:
        verbose_name = 'Калорийность'
        verbose_name_plural = 'Калорийности'


class UserRecipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')



    class Meta:
        unique_together = ('user', 'recipe')
        verbose_name = 'Рецепт пользователя'
        verbose_name_plural = 'Рецепты пользователей'

class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')
    category_name = models.CharField(max_length=255, verbose_name='Категория')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория рецепта'
        verbose_name_plural = 'Категории рецептов'
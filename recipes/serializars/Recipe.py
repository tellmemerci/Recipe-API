from rest_framework import serializers
from recipes.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    '''Сериализатор класса Recipes (Рецепты)'''
    class Meta:
        model = Recipe
        fields = '__all__'

    def validate_time_of_cooking(self, value):
        '''Использование валидации поля по врмемени готовки. Минимальное время приготовления - 10 минут'''

        if value < 10:
            raise serializers.ValidationError('Слишком маленькое значение для общего времени приготовления')
        return value

    def validate_calories(self, value):
        '''Проверка на то, сколько ккалорий. Минимальное количество - 1'''
        if value < 1:
            raise serializers.ValidationError('Не может блюдо быть меньше чем 1 ккал')
        return value

    def validate_name(self, value):
        '''Проверка на уникальность рецепта, получаем id и проверяем существует ли такой рецепт с таким же именем
        исключая текущий'''

        recipe_id = self.context.get('recipe_id')

        if recipe_id:
            if Recipe.objects.filter(name=value).exclude(id=recipe_id).exists():
                raise serializers.ValidationError(f'Рецепт с названием "{value}" уже существует.')
        else:
            if Recipe.objects.filter(name=value).exists():
                raise serializers.ValidationError(f'Рецепт с названием "{value}" уже существует.')
        return value
from rest_framework import serializers
from recipes.models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    '''Сериализатор для ингридиентов, которые хранятся на сайте (как список)'''
    class Meta:
        model = Ingredient
        fields = '__all__'


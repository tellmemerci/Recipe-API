from rest_framework import serializers
from recipes.models import RecipeIngredient


class RecipeIngredientSerializer(serializers.ModelSerializer):
    '''Сериализатор, для ингредиентов, которые в самом рецепте'''
    class Meta:
        model = RecipeIngredient
        fields = '__all__'

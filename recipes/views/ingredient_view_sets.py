from rest_framework import viewsets
from recipes.models import Ingredient
from recipes.serializars.Ingredients import IngredientSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    '''Вьюшка для рецептов, которые есть в базе данных'''
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

from rest_framework import viewsets
from recipes.models import Ingredient
from recipes.serializars.Ingredients import IngredientSerializer
from rest_framework.filters import SearchFilter

class IngredientViewSet(viewsets.ModelViewSet):
    '''Вьюшка для рецептов, которые есть в базе данных'''
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

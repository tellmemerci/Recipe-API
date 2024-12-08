from rest_framework import viewsets
from recipes.models import Ingredient
from recipes.serializars.Ingredients import IngredientSerializer
from recipes.views.filters.filter_by_ingredient import IngredientFilter

class IngredientViewSet(viewsets.ModelViewSet):
    '''Вьюшка для рецептов, которые есть в базе данных'''
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filterset_class = IngredientFilter
    search_fields = ['name']

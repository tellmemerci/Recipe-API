from rest_framework import viewsets
from django_filters import rest_framework as filters  # Импортируйте DjangoFilterBackend
from recipes.models import RecipeIngredient
from recipes.serializars.RecipeIngredient import RecipeIngredientSerializer
from recipes.views.filters.filter_by_recipe_ingredient import RecipeIngredientFilter

class RecipeIngredientViewSet(viewsets.ModelViewSet):
    '''Вьюшка для ингредиентов, которые находятся в рецепте'''
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = RecipeIngredientFilter



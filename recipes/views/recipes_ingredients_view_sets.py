from rest_framework import viewsets
from recipes.models import RecipeIngredient
from recipes.serializars.RecipeIngredient import RecipeIngredientSerializer


class RecipeIngredientViewSet(viewsets.ModelViewSet):
    '''Вьюшка для ингредиентов, которые находятся в рецепте'''
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer


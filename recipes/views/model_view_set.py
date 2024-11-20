from rest_framework import viewsets
from recipes.models import Recipe
from recipes.serializars.recipe import RecipeSerializer

class RecipeModelViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

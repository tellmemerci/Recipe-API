from rest_framework import viewsets
from recipes.models import Ingredient
from recipes.serializars.Ingredients import IngredientSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

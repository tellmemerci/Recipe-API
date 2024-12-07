from recipes.models import Ingredient
from django_filters import rest_framework as filters


class IngredientFilter(filters.FilterSet):
    class Meta:
        model = Ingredient
        fields = {
            'name': ['exact', 'icontains'],
        }
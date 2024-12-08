from django_filters import rest_framework as filters
from recipes.models import RecipeIngredient

class RecipeIngredientFilter(filters.FilterSet):
    min_amount = filters.NumberFilter(field_name='quantity', lookup_expr='gte')
    max_amount = filters.NumberFilter(field_name='quantity', lookup_expr='lte')

    class Meta:
        model = RecipeIngredient
        fields = ['min_amount', 'max_amount']
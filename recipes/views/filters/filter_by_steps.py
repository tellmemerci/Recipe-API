from django_filters import rest_framework as filters
from recipes.models import RecipeStep

class RecipeStepFilter(filters.FilterSet):
    '''Фильтрация по шагу в рецепте, показывает рецепты у которого есть этот шаг'''
    step_number = filters.NumberFilter(field_name='step_number', lookup_expr='exact')

    class Meta:
        model = RecipeStep
        fields = ['step_number']

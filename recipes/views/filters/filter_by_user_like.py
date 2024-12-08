from django_filters import rest_framework as filters
from recipes.models import RecipeLike
from recipes.models import Recipe

class RecipeLikeFilter(filters.FilterSet):

    '''Фильтрация для просмотра того, какие пользователи
    поставили лайк на определенный рецепт'''

    recipe = filters.ModelChoiceFilter(queryset=Recipe.objects.all())

    class Meta:
        model = RecipeLike
        fields = ['recipe']

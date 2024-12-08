from rest_framework import viewsets
from recipes.models import RecipeStep
from recipes.serializars.RecipeSteps import RecipeStepSerializer
from django_filters import rest_framework as filters
from recipes.views.filters.filter_by_steps import RecipeStepFilter

class RecipeStepViewSet(viewsets.ModelViewSet):
    '''Вьюшка для класса RecipeStep (отображает шаги рецептов)'''
    queryset = RecipeStep.objects.all()
    serializer_class = RecipeStepSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RecipeStepFilter
from rest_framework import viewsets
from recipes.models import RecipeStep
from recipes.serializars.RecipeSteps import RecipeStepSerializer

class RecipeStepViewSet(viewsets.ModelViewSet):
    '''Вьюшка для класса RecipeStep (отображает шаги рецептов)'''
    queryset = RecipeStep.objects.all()
    serializer_class = RecipeStepSerializer
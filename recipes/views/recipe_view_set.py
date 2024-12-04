from rest_framework import viewsets
from recipes.models import Recipe
from recipes.serializars.Recipe import RecipeSerializer

class RecipeModelViewSet(viewsets.ModelViewSet):
    '''Модель для отображения класса Reipe (Рецепты)'''
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_serializer(self, *args, **kwargs):
        '''Получение recipe ID для проверки уникальности в serializaes (recipe)'''

        if self.action == 'update':
            kwargs['context'] = {'recipe_id': self.kwargs['pk']}
        return super().get_serializer(*args, **kwargs)
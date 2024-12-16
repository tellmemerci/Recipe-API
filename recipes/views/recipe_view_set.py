from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.decorators import action
from recipes.models import Recipe
from recipes.serializars.Recipe import RecipeSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from  django.http import Http404

class RecipeModelViewSet(viewsets.ModelViewSet):
    '''Модель для отображения класса Reipe (Рецепты)'''
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_object(self):
        """Переопределение метода для получения объекта или возврата ошибки 404."""
        obj = get_object_or_404(Recipe, pk=self.kwargs.get('pk'))
        return obj


    @action(methods=["GET"], detail=False)
    def get_recipes(self, request):
        """
        Получение рецептов, которые НЕ являются публичными (ИЛИ) имеют статус "На модерации"
        (И) калорийность больше 500 (И) время приготовления меньше 40 минут
        """
        recipes_object = Recipe.objects.filter(
            (~Q(is_public=True) | Q(status_site='На модерации')) & Q(calories__gt=500) & Q(time_of_cooking__lt=40)
        )
        serializer = RecipeSerializer(recipes_object, many=True)
        return Response(serializer.data)

    @action(methods=["GET"], detail=False)
    def get_recipes_complex(self, request):
        """
        НЕ являются публичными ИЛИ статус равен "На модерации"
        И время приготовления меньше 60 минут
        И калорийность больше 300
        ИЛИ название содержит "салат" или "вегетарианский"
        """
        recipes = Recipe.objects.filter(
            (~Q(is_public=True) | Q(status_site='На модерации')) &
            Q(time_of_cooking__lt=60) &
            Q(calories__gt=300) &
            (Q(name__icontains='салат') | Q(name__icontains='вегетарианский'))
        )

        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False)
    def create_recipe(self, request):
        """Создание нового рецепта."""
        serializer = RecipeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





def get_serializer(self, *args, **kwargs):
        '''Получение recipe ID для проверки уникальности в serializaes (recipe)'''

        if self.action == 'update':
            kwargs['context'] = {'recipe_id': self.kwargs['pk']}
        return super().get_serializer(*args, **kwargs)




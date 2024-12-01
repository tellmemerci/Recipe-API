from datetime import timezone

from rest_framework import generics, status
from rest_framework.response import Response
from recipes.models import Recipe
from recipes.serializars.Recipe import RecipeSerializer
from django.db.models import Q
from rest_framework.decorators import action



class RecipeByTimeOfCooking(generics.ListAPIView):
    serializer_class = RecipeSerializer
    def get_queryset(self):
        '''Фильрация по времени приготовлению'''

        try:
            time_of_cooking = int(self.kwargs.get('time_of_cooking'))
            if time_of_cooking < 0 or time_of_cooking == 0:
                return Response({"error": "Внимание, ошибка! Время приготовления не может быть отрицательным или равен нулю!"}, status=status.HTTP_400_BAD_REQUEST)
            return Recipe.objects.filter(time_of_cooking=time_of_cooking)
        except (KeyError, ValueError) as e:
            return Response({"error": f"Invalid input: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from recipes.models import Recipe
from recipes.serializars.Recipe import RecipeSerializer


class RecipeDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        recipe = get_object_or_404(Recipe, pk=pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)

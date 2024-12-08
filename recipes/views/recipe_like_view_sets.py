from rest_framework import viewsets

from recipes.models import RecipeLike
from recipes.serializars.RecipeLike import RecipeLikeSerializer
from django_filters import rest_framework as filters
from recipes.views.filters.filter_by_user_like import RecipeLikeFilter


class RecipeLikeViewSet(viewsets.ModelViewSet):
    '''Вьюшка для просмотра лайков, которые ставят пользователи'''
    queryset = RecipeLike.objects.all()
    serializer_class = RecipeLikeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RecipeLikeFilter

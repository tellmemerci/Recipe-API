from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipes.views.view_sets import RecipeViewSet
from recipes.views.filter_by_time_of_cooking import RecipeByTimeOfCooking

router = DefaultRouter()
router.register('recipe-viewset', RecipeViewSet, basename='recipe-viewset')

urlpatterns = [
    path('', include(router.urls)),
    path('timecoocking/<int:time_of_cooking>/', RecipeByTimeOfCooking.as_view(), name='time_of_cooking'),
]


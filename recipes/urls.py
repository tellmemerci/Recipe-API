from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipes.views.view_sets import RecipeViewSet


router = DefaultRouter()
router.register('recipe-viewset', RecipeViewSet, basename='recipe-viewset')

urlpatterns = [
    path('', include(router.urls)),
]


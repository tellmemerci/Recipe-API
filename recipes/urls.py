from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
import recipes
from recept.urls import schema_view
from recipes.views.recipe_view_set import RecipeModelViewSet
from recipes.views.recipe_like_view_sets import RecipeLikeViewSet
from recipes.views.recipes_steps_view_sets import RecipeStepViewSet
from recipes.views.recipes_ingredients_view_sets import RecipeIngredientViewSet
from recipes.views.ingredient_view_sets import IngredientViewSet
import recipes.views.task_view as task_view
import recipes
from recipes.views.recipe_view_set import RecipeModelViewSet
from recipes.views.recipe_like_view_sets import RecipeLikeViewSet
from recipes.views.recipes_steps_view_sets import RecipeStepViewSet
from .views.recipes_ingredients_view_sets import RecipeIngredientViewSet
from .views.ingredient_view_sets import IngredientViewSet
import recipes.views.task_view as task_view


router = DefaultRouter()
router.register('recipe-viewset', RecipeModelViewSet, basename='recipe-viewset')
router.register('recipe_steps-viewset', RecipeStepViewSet, basename='recipe-steps-viewset')
router.register('recipe-ingredient', RecipeIngredientViewSet, basename='recipe-ingredient')
router.register('ingredient', IngredientViewSet, basename='ingredient')
router.register('recipe-like', RecipeLikeViewSet, basename='recipe-like')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('home/', task_view.home, name='home'),

    # Include REST framework router URLs
    path('', include(router.urls)),
    ]


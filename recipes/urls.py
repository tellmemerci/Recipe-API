from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipes.views.recipe_view_set import RecipeModelViewSet
from recipes.views.recipe_like_view_sets import RecipeLikeViewSet
from recipes.views.recipes_steps_view_sets import RecipeStepViewSet
from .views.recipes_ingredients_view_sets import RecipeIngredientViewSet
from .views.ingredient_view_sets import IngredientViewSet

router = DefaultRouter()
router.register('recipe-viewset', RecipeModelViewSet, basename='recipe-viewset')
router.register('recipe_steps-viewset', RecipeStepViewSet, basename='recipe-steps-viewset')
router.register('recipe-ingredient', RecipeIngredientViewSet, basename='recipe-ingredient')
router.register('ingredient', IngredientViewSet, basename='ingredient')
router.register('recipe-like', RecipeLikeViewSet, basename='recipe-like')

urlpatterns = [
    path('', include(router.urls)),

]


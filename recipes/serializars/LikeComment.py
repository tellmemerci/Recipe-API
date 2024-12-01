from rest_framework import serializers
from recipes.models import RecipeLike, RecipeComment


class LikeRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeLike
        fields = '__all__'


class CommentRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeComment
        fields = '__all__'
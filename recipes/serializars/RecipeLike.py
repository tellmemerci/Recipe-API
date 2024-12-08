from rest_framework import serializers
from recipes.models import RecipeLike


class RecipeLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeLike
        fields = '__all__'
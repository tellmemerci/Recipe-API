from rest_framework import serializers
from recipes.models import RecipeStep

class RecipeStepSerializer(serializers.ModelSerializer):
    '''Сериализатор для Шагов Рецепта'''
    class Meta:
        model = RecipeStep
        fields = '__all__'

    def validate_step_number(self, value):
        '''Валидация номера шага в рецепте. На отрицание или равным нулю'''
        if value < 1 :
            raise serializers.ValidationError('Номер шага не может быть отрицательным или равным нулю')
        return value
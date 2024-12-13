# Generated by Django 4.2.16 on 2024-12-12 14:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0015_recipe_ingredients_alter_ingredient_measurement_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalrecipecomment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='recipecomment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

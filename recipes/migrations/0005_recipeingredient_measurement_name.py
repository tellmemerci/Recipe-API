# Generated by Django 5.0.3 on 2024-11-07 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipecomment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredient',
            name='measurement_name',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]

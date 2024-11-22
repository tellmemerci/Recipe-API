from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from simple_history.admin import SimpleHistoryAdmin
from .export import RecipeResource
from .models import User, Recipe, RecipeIngredient, RecipeStep, RecipeLike, RecipeComment, Calories, UserRecipes, RecipeCategory, Ingredient

@admin.register(RecipeCategory)
class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'category_name')
    list_filter = ('recipe', 'category_name')


    @admin.display(description='Custom Display')
    def category_name(self, obj):
        return f"Custom: {obj.recipe.category.name}"

@admin.register(RecipeComment)
class RecipeCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'text', 'status')
    list_filter = ('user', 'recipe', 'status')
    date_hierarchy = 'created_at'
    list_display_links = ('user', 'text', 'recipe', 'status')
    raw_id_fields = ('user', 'recipe')
    search_fields = ('user', 'status')
    #readonly_fields = ('text', 'created_at')

class RecipeAdmin(SimpleHistoryAdmin, ImportExportActionModelAdmin):
    list_display = ('name', 'adversting_text', 'status_site')
    history_list_display = ['status']
    search_fields = ('name', 'adversting_text')
    list_filter = ('status_site',)
admin.site.register(Recipe, RecipeAdmin)

@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'step_number', 'description')
    list_filter = ('recipe', 'step_number')
    search_fields = ('recipe',)


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'quantity', 'get_measurement_unit')
    search_fields = ('recipe', 'ingredient')

    def get_measurement_unit(self, obj):
        """Метод для отображения единицы измерения."""
        try:
            return obj.ingredient.measurement_name
        except Ingredient.DoesNotExist:
            return "Нет данных"
    get_measurement_unit.short_description = 'Единица измерения'

    def quantity_with_unit(self, obj):
        try:
            measurement_unit = obj.ingredient.measurement_name
            return f"{obj.quantity} {measurement_unit}"
        except Ingredient.DoesNotExist:
            return "Нет данных"

    quantity_with_unit.short_description = "Количество и единица"

@admin.register(UserRecipes)
class UserRecipesAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


@admin.register(RecipeLike)
class RecipeLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('recipe', 'user')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role')
    search_fields = ('username', 'role',)

@admin.register(Calories)
class CaloriesAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'protein', 'fat', 'carbohydrates')
    search_fields = ('recipe',)

@admin.register(Ingredient)
class Admin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'measurement_name')
    list_filter = ('measurement_name',)



admin.site.site_header = 'Администрирование сайта рецептов'
admin.site.site_title = 'Панель администратора'
admin.site.index_title = 'Добро пожаловать в админ-панель'
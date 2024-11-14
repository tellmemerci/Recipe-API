from django.contrib import admin
from .models import User, Recipe, RecipeIngredient, RecipeStep, RecipeLike, RecipeComment, Calories, UserRecipes, RecipeCategory

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
    date_hierarchy = 'created_at'
    list_display_links = ('user', 'text', 'recipe', 'status')
    raw_id_fields = ('user', 'recipe')
    #readonly_fields = ('text', 'created_at')

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'adversting_text')
    search_fields = ('name', 'adversting_text')

@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'step_number', 'description')


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient_name', 'quantity', 'measurement_name')

@admin.register(UserRecipes)
class UserRecipesAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


@admin.register(RecipeLike)
class RecipeLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role')

@admin.register(Calories)
class CaloriesAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'protein', 'fat', 'carbohydrates')

admin.site.site_header = 'Администрирование сайта рецептов'
admin.site.site_title = 'Панель администратора'
admin.site.index_title = 'Добро пожаловать в админ-панель'
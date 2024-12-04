from import_export.formats.base_formats import XLSX
from import_export.resources import ModelResource
from recipes.models import Recipe
class RecipeResource(ModelResource):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'adversting_text', 'status_site', 'time_of_cooking')
        formats = [XLSX]


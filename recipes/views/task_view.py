from django.http import HttpResponse
import recipes.tasks as tasks
def home(request):
    tasks.downoload_a_cat.delay()
    return HttpResponse('<h1> TESTING </h1>')
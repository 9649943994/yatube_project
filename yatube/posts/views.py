from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponses('Главная страница')

def group_posts(requests, slug):
    return HttpResponse(F'Группы постов{slug')
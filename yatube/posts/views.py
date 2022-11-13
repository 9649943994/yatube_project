from django.http import HttpResponse

# Create your views here.

def index(requests):
    return HttpResponse('Главная страница')

def group_posts(requests, slug):
    return HttpResponse(f'Группы постов,{slug}')
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    template = 'posts/index.html'
    return render(request, template)


def group_list(request):
    return HttpResponse('Список групп')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_detail(request, slug):
    return HttpResponse(f'Группа {slug}')
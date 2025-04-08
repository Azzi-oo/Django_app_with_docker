from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'float': 20.56,
        'lst': ['1', '2', '3'],
    }
    return render(request, 'women/index.html', context=data)


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")    


def archive(request, year):
    if year > 2023:
        url = reverse('cats', args=('music', ))
        return HttpResponseRedirect('/')
    return HttpResponse(f"<h1>Архив по годам</h1><p>year: {year}</p>")


def about(request):
    return render(request, 'women/about.html', {'title': 'О нас', 'cat': 'Музыка'})


def pageNotFound(request, exception):
    return render(request, 'women/about.html')
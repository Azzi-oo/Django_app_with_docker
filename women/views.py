from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.template.loader import render_to_string

from women.models import Category, TagPost, Women


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    posts = Women.objects.all()
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


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk)
    data = {
        'title': f'Рубрика {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'women/about.html')


def show_post(request, post_slug):
    post = get_object_or_404(Women, pk=post_slug)
    
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    
    return render(request, 'women/post_html.html', data)

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Autotization")

def addpage(request):
    return HttpResponse("Добавление статьи")

def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED)
    
    data = {
        'title': f'Tag: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }
    
    return render(request, 'women/index.html', context=data)


from django.urls import path, re_path, register_converter

from config.urls import catalog
from women.converters import FourDigitYearConverter

from . import views

register_converter(FourDigitYearConverter, "year")

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("cats/<int:cat_id>/", views.categories, name="cats_id"),
    path('contact/', views.contact, name='contact'),
    path("post/<slug:post_slug>/", views.show_post, name="post"),
    path("login/", views.login, name="login"),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='tag'),
]

# urlpatterns = [
#     path("women/cat/", catalog),# здесь с помощью функции path() прописывайте новый маршрут
# ]
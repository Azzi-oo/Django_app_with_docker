from django.urls import path, re_path, register_converter

from config.urls import catalog
from women.converters import FourDigitYearConverter

from . import views

register_converter(FourDigitYearConverter, "year")

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("cats/<int:cat_id>/", views.categories, name="cats_id"),
    path("cats/<slug:cat_slug>/", views.categories_by_slug, name="cats_slug"),
    re_path("archive/<year4:year>/", views.archive, name="archive"),
]

# urlpatterns = [
#     path("women/cat/", catalog),# здесь с помощью функции path() прописывайте новый маршрут
# ]
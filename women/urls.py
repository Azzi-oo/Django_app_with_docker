from django.urls import path, re_path, register_converter

from config.urls import catalog
from women.converters import FourDigitYearConverter

from . import views

register_converter(FourDigitYearConverter, "year")

urlpatterns = [
    path("", views.index),
    path("cats/<int:cat_id>/", views.categories),
    path("cats/<slug:cat_slug>/", views.categories_by_slug),
    re_path("archive/<year4:year>/", views.archive),
]

# urlpatterns = [
#     path("women/cat/", catalog),# здесь с помощью функции path() прописывайте новый маршрут
# ]
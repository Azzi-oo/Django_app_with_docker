from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse


def catalog(request):
    return HttpResponse("catalog")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("women.urls")),
]    
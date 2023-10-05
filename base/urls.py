
from django.contrib import admin
from django.urls import path
from base.views import bienvenidos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenidos, name="inicio"),
]

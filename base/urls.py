
from django.contrib import admin
from django.urls import path
from base.views import bienvenidos, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenidos, name="inicio"),
    path('login/', login, name="login"),
    
]

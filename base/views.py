from django.shortcuts import render

def bienvenidos(request):
    titulo= "inicio"
    context={
        "titulo": titulo,
    }
    return render(request, 'index.html', context)

def login(request):
    titulo= "inicio de sesión"
    context={
        "titulo": titulo,
    }
    return render(request, 'login.html', context)


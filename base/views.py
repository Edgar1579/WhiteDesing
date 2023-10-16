from django.shortcuts import render

def bienvenidos(request):
    titulo= "inicio"
    context={
        "titulo": titulo,
    }
    return render(request, 'index.html', context)
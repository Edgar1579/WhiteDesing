from django.shortcuts import render

def bienvenidos(request):
    context={
        
    }
    return render(request, 'index.html', context)
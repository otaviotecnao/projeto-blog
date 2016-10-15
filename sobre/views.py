from django.shortcuts import render

# Create your views here.

def sobre_nos(request):
    return render(request, 'sobre/sobre_nos.html')

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def firstview(request):
    data ={
        "name" : "hola"
    }
    return render(request, 'index.html', data)


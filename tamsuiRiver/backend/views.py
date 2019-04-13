from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Hello, world. You're at the backend index.")

def browse(request):
    return render(request, 'browse.html')

def producer(request):
    return render(request, 'producer.html')

def signup(request):
    return render(request, 'signup.html')
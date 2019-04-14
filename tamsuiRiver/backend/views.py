from django.shortcuts import render, redirect

from django.http import HttpResponse
from backend.models import Company, Request, Farmer

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Hello, world. You're at the backend index.")

def browse(request):
    requests = Request.objects.all()
    return render(request, 'browse.html', {'requests':requests})

def producer(request):
    if request.method == 'GET':
        return render(request, 'producer.html')
    
    elif request.method == 'POST':
        company = "HKUST"
        item = request.POST.get('item')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        farmer = ""

        request = Request()
        request.company = company
        request.item = item
        request.price = price
        request.quantity = quantity
        request.farmer = farmer

        request.save()
        return redirect('/submitted/')


def signin(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    
    elif request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        
        if Company.objects.all().filter(name=name):
            return redirect('/producer/')
        else:
            return redirect('/index/')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        product = request.POST.get('product')
        origin = request.POST.get('origin')
        certificate = request.POST.get('certificate')
        description = request.POST.get('description')

        farmer = Farmer()
        farmer.name = name
        farmer.email = email
        farmer.password = password
        farmer.product = product
        farmer.origin = origin
        farmer.certificate = certificate
        farmer.description = description

        farmer.save()
        return redirect('/index/')


def submitted(request):
    return render(request, 'success.html')


def pending(request):
    return render(request, 'pending.html')


def preorder(request):
    return render(request, 'preorder.html')
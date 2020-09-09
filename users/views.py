from django.shortcuts import render

def homepage(request):
    return render(request, 'users/index.html')

def login(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/login.html')

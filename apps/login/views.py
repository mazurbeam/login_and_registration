from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

# Create your views here.

def index(request):
    return render(request, 'login/index.html')

def register(request):
    results = User.objects.registerValidation(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
    else:
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = request.POST['password'])
        messages.success(request, 'User has been created. Please log in.')
    return redirect('/')

def login(request):
    results = User.objects.loginValidation(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
    else:
        user = User.objects.get(email = request.POST['email'])
        messages.success(request, "Login Succesful!")
    return redirect('/')

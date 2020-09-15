from django.shortcuts import render
from django.contrib import auth



def home(request):
    auth.logout(request)
    return render(request, 'home.html')

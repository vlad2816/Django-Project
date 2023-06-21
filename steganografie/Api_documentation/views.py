from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'Api_documentation/home.html')


def criptare(request):
    return render(request, 'Api_documentation/criptare.html')

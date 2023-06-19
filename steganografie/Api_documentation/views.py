from django.shortcuts import render
from django.http import HttpResponse


foto = [
    {
        'id': 1,
        'Nume': 'Harry Potter',
        'Status': True
    },
    {

        'id': 2,
        'Nume': 'Spiderman',
        'Status': False

    },
    {

        'id': 3,
        'Nume': 'Copilarie',
        'Status': True

    }
]


def home(request):
    context = {'foto': foto}
    return render(request, 'Api_documentation/home.html', context)


def criptare(request):
    return render(request, 'Api_documentation/criptare.html')

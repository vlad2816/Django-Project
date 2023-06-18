from django.shortcuts import render
from django.http import HttpResponse


fotografii = [
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
    context = {'fotografii': fotografii}
    return render(request, 'Api_documentation/home.html', context)


def criptare(request):
    return render(request, 'Api_documentation/criptare.html')

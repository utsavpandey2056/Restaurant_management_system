# I have created this file - Utsav
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

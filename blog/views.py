from django.shortcuts import render
from django.http import HttpResponse

def index (request):
        return render (request, 'index.html')

def about (request):
        return render (request, 'about.html')

def fitbit (request):
        return render (request, 'fitbit.html')

def tut1 (request):
        return render (request, 'fitbit/tut1.html')


# Create your views here.

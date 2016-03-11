from django.shortcuts import render
from django.http import HttpResponse

def index (request):
        return render (request, 'index.html')

def about (request):
        return render (request, 'about.html')

def fitbit (request):
        return render (request, 'fitbit/fitbit.html')

def fitbit_blog (request):
        return render (request, 'fitbit/fitbit_blog.html')

def fitbit_article_1 (request):
        return render (request, 'fitbit/tutoria1.html')

def fitbit_article_2 (request):
        return render (request, 'fitbit/tutorial2.html')

def technology (request):
        return render (request, 'technology/technology.html')

def environment (request):
        return render (request, 'environment/environment.html')


# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def index (request):
        return render (request, 'index.html')

def about (request):
        return render (request, 'about.html')

def blog (request):
        return render (request, 'blog.html')

def fitbit (request):
        return render (request, 'fitbit/fitbit.html')

def fitbit_blog (request):
        return render (request, 'blog_pages/fitbit/fitbit_blog.html')

def fitbit_blog_entry (request, entry):
        print entry
        return render (request, 'blog_pages/fitbit/articles/'+entry+'.html')

def technology (request):
        return render (request, 'blog_pages/technology/technology.html')

def technology_blog_entry (request, entry):
        return render (request, 'blog_pages/technology/articles/'+entry+'.html')

def environment (request):
        return render (request, 'blog_pages/environment/environment.html')

def environment_blog_entry (request, entry):
        return render (request, 'blog_pages/environment/articles/'+entry+'.html')

def life (request):
        return render (request, 'life/life.html')

# Create your views here.

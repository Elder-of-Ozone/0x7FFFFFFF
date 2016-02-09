from django.shortcuts import render
from django.http import HttpResponse

def page (request):
        return HttpResponse ("Hello World!")
# Create your views here.

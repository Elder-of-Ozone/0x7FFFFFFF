from django.http import HttpResponse
from django.shortcuts import render

def page (request):

    return render (request, 'index.html')

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request, *args, **kwargs):
    return render(request, 'index.html', {})

def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})

def elements_view(request, *args, **kwargs):
    return render(request, 'elements.html', {})
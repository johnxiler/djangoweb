from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'blog.html')


def about(request):
    return render(request, 'about.html')


def features(request):
    return render(request, 'features.html')


def contact(request):
    return render(request, 'contact.html')

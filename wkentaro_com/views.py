from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template_name = 'index.html'
    return render(request, template_name, {'page_name': 'index'})


def about(request):
    template_name = 'about.html'
    return render(request, template_name, {'page_name': 'about'})


def research(request):
    template_name = 'research.html'
    return render(request, template_name, {'page_name': 'research'})

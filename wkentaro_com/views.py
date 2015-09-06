from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    template_name = 'index.html'
    return render(request, template_name)

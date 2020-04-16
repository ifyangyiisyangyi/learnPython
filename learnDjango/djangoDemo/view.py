from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context         = {}
    context['hello'] = 'Hello World!'
    context['inc'] = 'include test~'
    return render(request, 'hello.html', context)

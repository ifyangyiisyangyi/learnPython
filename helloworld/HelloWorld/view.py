from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'hello nicolas junjie!'
    return render(request, 'hello.html', context)

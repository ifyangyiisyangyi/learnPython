from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.
from article.models import Article


def test(request):
    body = model_to_dict(Article.objects.get(id=1))
    print(body)
    return render(request, 'detail.html', {'body' : body})
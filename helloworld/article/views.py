from django.conf import settings
from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.
from django.views import generic

from article.models import Article


def test(request):
    body = model_to_dict(Article.objects.get(id=1))
    print(body)
    return render(request, 'blog/detail.html', {'body' : body})



class IndexView(generic.ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = getattr(settings, 'BASE_PAGE_BY', None)
    paginate_orphans = getattr(settings, 'BASE_ORPHANS', 0)

    def get_ordering(self):
        sort = self.kwargs.get('sort')
        if sort == 'v':
            return ('-views', '-update_date', '-id')
        return ('-is_top', '-create_date')
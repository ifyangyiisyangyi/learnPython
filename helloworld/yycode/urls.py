from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf.urls import url
from django.urls import path

from . import view, spider
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', view.login, name='home'),
    path('save_message/', view.save_message, name='save_message'),
    path('article_spider/', spider.article_spider),
    path('article_show/', view.article_show, name='article_show'),
    path('test/', view.test, name='test'),
]

urlpatterns += staticfiles_urlpatterns()

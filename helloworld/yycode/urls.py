from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf.urls import url
from django.urls import path, include
from . import views, spider
from django.contrib import admin
from .views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='home'),

    path('save_message/', views.save_message, name='save_message'),
    path('article_spider/', spider.article_spider),
    path('article_show/', views.article_show, name='article_show'),
    path('article/', include('article.urls')),
]

urlpatterns += staticfiles_urlpatterns()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from . import testdb, view, spider
from django.contrib import admin

urlpatterns = [
    url(r'^$', view.login),
    # url(r'^register$', testdb.add_user),
    url(r'^admin/', admin.site.urls),
    # url(r'^login/', view.login),
    url(r'^save_message', view.save_message),
    url(r'^article_spider', spider.article_spider),
    url(r'^article_show/', view.article_show, name='article_show'),
    url(r'^test/', view.test, name='test'),
]

urlpatterns += staticfiles_urlpatterns()

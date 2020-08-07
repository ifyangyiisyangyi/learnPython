from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from . import testdb, view
from django.contrib import admin

urlpatterns = [
    url(r'^$', view.show_404),
    url(r'^register$', testdb.add_user),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', view.login),
    url(r'^save_message', view.save_message),
    url(r'^article_spider', view.article_spider),
]

urlpatterns += staticfiles_urlpatterns()

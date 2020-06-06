from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

from django.conf.urls import url
from . import testdb, view
from django.contrib import admin

urlpatterns = [
    url(r'^$', view.show_404),
    url(r'^register$', testdb.add_user),
    url(r'^admin/', admin.site.urls),
    url(r'^qq/', view.test_qq),
    url(r'^result/', view.result_qq),
    url(r'^getEmail/', view.user),
    url(r'^game/', view.game),
    url(r'^gameResult', view.gameResult),
    url(r'^login', view.login),
]



urlpatterns += staticfiles_urlpatterns()
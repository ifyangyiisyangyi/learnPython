from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

from django.conf.urls import url
from . import testdb, view
from django.contrib import admin

urlpatterns = [
    url(r'^$', view.hello),
    url(r'^register$', testdb.add_user),
    url(r'^admin/', admin.site.urls),
    url(r'^qq/', view.test_qq),
    url(r'^result/', view.result_qq),
    url(r'^getEmail/', view.user),

]



urlpatterns += staticfiles_urlpatterns()
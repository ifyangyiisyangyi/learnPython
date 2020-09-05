from django.urls import path
from .views import Cbvdemo, Toolview

urlpatterns = [
    path('Cbvdemo', Cbvdemo.as_view()),
    path('', Toolview, name='total'),

]

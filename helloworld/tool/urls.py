from django.urls import path
from .views import Cbvdemo

urlpatterns = {
    path('Cbvdemo', Cbvdemo.as_view()),

}
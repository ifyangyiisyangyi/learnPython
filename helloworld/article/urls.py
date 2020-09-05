from django.urls import path
from . import views
from .views import IndexView

app_name = 'article'
urlpatterns = [
    # path('hello', IndexView.as_view(), name='index_2'),  # 主页，自然排序
    path('test/', views.test, name='test'),
    path('', IndexView.as_view(), name='index'),  # 主页，自然排序
]

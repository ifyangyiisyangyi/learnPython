from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    # path('hello', IndexView.as_view(), name='index_2'),  # 主页，自然排序
    path('test/', views.test, name='test'),
]

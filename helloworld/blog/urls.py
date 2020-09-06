from django.urls import path
from .views import IndexView, DetailView, CategoryView, TagView

app_name = 'blog'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # 主页，自然排序
    path('article/<slug:slug>/', DetailView.as_view(), name='detail'),  # 文章内容页
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('tag/<slug:slug>/', TagView.as_view(), name='tag'),
]

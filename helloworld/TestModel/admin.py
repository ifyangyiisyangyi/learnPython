# admin.py

from django.contrib import admin
from TestModel import models

admin.site.site_header = 'yy 项目管理系统'
admin.site.site_title = '登录系统后台'
admin.site.index_title = '后台管理'


class ControlArticle(admin.ModelAdmin):
    '''自定义列表中栏目 添加list_display 属性'''
    list_display = ("title", "linkage", "tag")  # 设置显示的字段
    # 搜索条件title
    search_fields = ("title",)

    # 激活过滤器
    list_filter = ('tag', 'create_time')


admin.site.register(models.spider_article, ControlArticle)  # 注册到admin

# admin.py

from django.contrib import admin
from TestModel import models

admin.site.site_header = 'yy 项目管理系统'
admin.site.site_title = '登录系统后台'
admin.site.index_title = '后台管理'

class ControlUser(admin.ModelAdmin):
    '''自定义列表中栏目 添加list_display 属性'''
    list_display = ('user_name', 'user_pwd', 'user_mail')   # 设置显示的字段
    # 搜索条件user_name
    search_fields = ('user_name',)

# User表
admin.site.register(models.User, ControlUser)


class ControlArticle(admin.ModelAdmin):
    # 显示的字段
    list_display = ('title', 'body', 'auth', 'create_time', 'update_time')
    # 搜索条件
    search_fields = ('title',)
# 注册Article表
admin.site.register(models.Article, ControlArticle)



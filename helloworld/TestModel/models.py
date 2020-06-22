# models.py
# -*-coding:UTF-8-*-
from django.db import models


class User(models.Model):
    '''注册表'''
    user_name = models.CharField(max_length=30, primary_key=True)
    user_pwd = models.CharField(max_length=30)
    user_mail = models.CharField(max_length=30)

    # def __str__(self):
    #     return self.__doc__ + ":user_name --> " + self.user_name


class Message(models.Model):
    '''留言表'''
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    message = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now_add=True)


class Blog(models.Model):
    '''博客表'''
    blog_title = models.CharField(max_length=30)
    blog_date = models.DateField()
    blog_content = models.TextField()


class Article(models.Model):
    '''文章表'''
    title = models.CharField(verbose_name="文章标题", max_length=150)
    linkage = models.CharField(verbose_name="文章链接", max_length=150)
    tag = models.CharField(verbose_name="标签", max_length=150)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now_add=True)

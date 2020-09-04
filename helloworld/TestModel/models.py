# models.py
# -*-coding:UTF-8-*-
from django.db import models


class Message(models.Model):
    '''留言表'''
    ip = models.CharField(max_length=300, blank=True)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    message = models.CharField(max_length=300)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now_add=True)


class Blog(models.Model):
    '''博客表'''
    blog_title = models.CharField(max_length=300)
    blog_content = models.TextField()
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now_add=True)


class spider_article(models.Model):
    '''文章表'''
    title = models.CharField(verbose_name="文章标题", max_length=300)
    linkage = models.CharField(verbose_name="文章链接", max_length=300)
    tag = models.CharField(verbose_name="标签", max_length=300)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now_add=True)


class Vistor(models.Model):
    '''访问者'''
    ip = models.CharField(verbose_name="访问ip", max_length=300)
    user_agent = models.CharField(verbose_name="user_agent", max_length=300, blank=True)
    country = models.CharField(verbose_name="user_agent", max_length=300, blank=True)
    city = models.CharField(verbose_name="user_agent", max_length=300, blank=True)
    ip_as = models.CharField(verbose_name="user_agent", max_length=300, blank=True)
    isp = models.CharField(verbose_name="user_agent", max_length=300, blank=True)
    count = models.IntegerField(verbose_name="访问次数", default=0)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now_add=True)

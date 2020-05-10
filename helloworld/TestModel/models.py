# models.py
# -*-coding:UTF-8-*-
from django.db import models


class User(models.Model):
    '''注册表'''
    user_name = models.CharField(max_length=30, primary_key=True)
    user_pwd = models.CharField(max_length=30)
    user_mail = models.CharField(max_length=30)

    def __str__(self):
        return self.__doc__ + ":user_name --> " + self.user_name




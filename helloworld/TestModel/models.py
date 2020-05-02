# models.py
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()


class User(models.Model):
    user_name = models.CharField(max_length=30, primary_key=True)
    user_pwd = models.CharField(max_length=30)
    user_mail = models.CharField(max_length=30)

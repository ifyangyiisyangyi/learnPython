# Generated by Django 3.0.5 on 2020-05-02 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0004_auto_20200502_1452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='mail',
            new_name='user_mail',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='pwd',
            new_name='user_pwd',
        ),
    ]

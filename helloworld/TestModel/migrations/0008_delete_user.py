# Generated by Django 3.0.5 on 2020-05-05 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0007_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]

# Generated by Django 3.0.5 on 2020-05-02 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('pwd', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=30)),
            ],
        ),
    ]

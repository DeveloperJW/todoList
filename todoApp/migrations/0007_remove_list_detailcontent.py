# Generated by Django 2.0.6 on 2018-07-22 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0006_auto_20180722_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='detailContent',
        ),
    ]
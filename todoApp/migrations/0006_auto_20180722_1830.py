# Generated by Django 2.0.6 on 2018-07-22 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0005_list_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='detail',
            new_name='detailContent',
        ),
    ]
# Generated by Django 2.0.6 on 2018-07-25 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0010_auto_20180724_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='detail',
            field=models.TextField(blank=True, default='No details has been added.'),
        ),
    ]

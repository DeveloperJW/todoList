# Generated by Django 2.0.6 on 2018-07-17 23:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0003_list_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='addedTime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

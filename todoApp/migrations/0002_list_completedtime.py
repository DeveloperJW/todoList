# Generated by Django 2.0.6 on 2018-07-13 21:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='completedTime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.1.4 on 2024-12-11 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='user',
        ),
    ]

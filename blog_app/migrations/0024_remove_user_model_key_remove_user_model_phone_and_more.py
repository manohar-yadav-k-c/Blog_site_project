# Generated by Django 4.2 on 2023-07-07 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0023_user_model_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_model',
            name='key',
        ),
        migrations.RemoveField(
            model_name='user_model',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='user_model',
            name='secret_name',
        ),
    ]

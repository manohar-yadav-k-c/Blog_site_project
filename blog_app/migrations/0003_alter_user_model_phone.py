# Generated by Django 4.2 on 2023-05-20 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_user_model_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='phone',
            field=models.PositiveIntegerField(),
        ),
    ]
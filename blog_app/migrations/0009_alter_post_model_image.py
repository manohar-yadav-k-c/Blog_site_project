# Generated by Django 4.2 on 2023-05-20 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_post_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_model',
            name='image',
            field=models.ImageField(upload_to='blog_img/'),
        ),
    ]

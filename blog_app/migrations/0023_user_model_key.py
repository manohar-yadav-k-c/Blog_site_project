# Generated by Django 4.2 on 2023-05-27 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0022_remove_post_model_subtitle_alter_post_model_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_model',
            name='key',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

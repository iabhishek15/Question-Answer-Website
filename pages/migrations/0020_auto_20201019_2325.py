# Generated by Django 2.2 on 2020-10-19 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_auto_20201019_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='replied_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replied_user', to=settings.AUTH_USER_MODEL),
        ),
    ]

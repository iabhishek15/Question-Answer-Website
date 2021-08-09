# Generated by Django 2.2 on 2020-10-19 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20201019_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_parent', to='pages.Comments'),
        ),
        migrations.AddField(
            model_name='comments',
            name='replied_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replied_comment', to='pages.Comments'),
        ),
        migrations.DeleteModel(
            name='Comment_reply',
        ),
    ]

# Generated by Django 2.2 on 2020-10-14 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20201014_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allquestion',
            name='downvote',
            field=models.ManyToManyField(blank=True, to='pages.DownVote'),
        ),
        migrations.AlterField(
            model_name='allquestion',
            name='upvote',
            field=models.ManyToManyField(blank=True, to='pages.UpVote'),
        ),
    ]
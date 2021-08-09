# Generated by Django 2.2 on 2020-10-15 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20201015_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allquestion',
            name='downvote',
        ),
        migrations.AddField(
            model_name='allquestion',
            name='downvote',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='allquestion',
            name='upvote',
        ),
        migrations.AddField(
            model_name='allquestion',
            name='upvote',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='allquestion',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
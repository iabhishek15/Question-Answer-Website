# Generated by Django 2.2 on 2020-10-14 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20201011_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='DownVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UpVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='allquestion',
            name='downvote',
        ),
        migrations.RemoveField(
            model_name='allquestion',
            name='upvote',
        ),
        migrations.AddField(
            model_name='allquestion',
            name='downvote',
            field=models.ManyToManyField(to='pages.DownVote'),
        ),
        migrations.AddField(
            model_name='allquestion',
            name='upvote',
            field=models.ManyToManyField(to='pages.UpVote'),
        ),
    ]

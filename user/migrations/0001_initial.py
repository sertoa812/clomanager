# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Detail', models.FileField(upload_to='')),
                ('Time', models.DateTimeField()),
                ('Accepted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Detail', models.TextField()),
                ('Time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Title', models.CharField(max_length=30)),
                ('Detail', models.CharField(max_length=255)),
                ('Time', models.DateTimeField()),
                ('Solved', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Detail', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('TypeFocus', models.CharField(max_length=255)),
                ('scores', models.IntegerField(default='100')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('realname', models.CharField(default='无', max_length=20)),
                ('email', models.CharField(default='无', max_length=255)),
                ('phone', models.CharField(default='无', max_length=30)),
                ('password', models.CharField(max_length=10)),
                ('LastLogin', models.DateTimeField()),
                ('TimesLogin', models.IntegerField(verbose_name=4)),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='UserID',
            field=models.ForeignKey(to='user.Users', related_name='userinfo_user_id'),
        ),
        migrations.AddField(
            model_name='questions',
            name='AskUserID',
            field=models.ForeignKey(to='user.Users', related_name='question_user_id'),
        ),
        migrations.AddField(
            model_name='questions',
            name='TypeID',
            field=models.ForeignKey(to='user.Type', related_name='question_type_id'),
        ),
        migrations.AddField(
            model_name='information',
            name='UserID',
            field=models.ForeignKey(to='user.Users', related_name='information_user_id'),
        ),
        migrations.AddField(
            model_name='answer',
            name='QuestionID',
            field=models.ForeignKey(to='user.Questions', related_name='answer_question_id'),
        ),
        migrations.AddField(
            model_name='answer',
            name='UserID',
            field=models.ForeignKey(to='user.Users', related_name='answer_user_id'),
        ),
    ]

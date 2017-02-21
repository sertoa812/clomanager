# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_questions_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='Title',
            field=models.CharField(default='这是一个问题的描述', max_length=30),
        ),
    ]

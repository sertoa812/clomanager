# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('Detail', models.FileField(upload_to='')),
                ('Time', models.DateTimeField()),
                ('Note', models.CharField(max_length=255, default='无')),
            ],
        ),
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, default='无')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('User', models.IntegerField(verbose_name=4)),
                ('Menu', models.IntegerField(verbose_name=4)),
                ('Detail', models.CharField(max_length=30, default='无')),
                ('Wardrobe', models.ForeignKey(to='wardrobe.MainMenu', related_name='wardrobe_id')),
            ],
        ),
        migrations.AddField(
            model_name='clothes',
            name='Menu',
            field=models.ForeignKey(to='wardrobe.Menu', related_name='menu_id'),
        ),
    ]

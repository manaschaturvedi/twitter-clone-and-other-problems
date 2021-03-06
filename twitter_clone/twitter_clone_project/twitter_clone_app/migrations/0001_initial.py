# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-30 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('tweet_body', models.CharField(max_length=140)),
                ('retweet_count', models.IntegerField()),
                ('likes_count', models.IntegerField()),
                ('replies_count', models.IntegerField()),
                ('is_deleted', models.IntegerField()),
                ('published_datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

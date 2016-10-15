# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 19:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Assemblage', '0002_auto_20161014_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelingroup',
            name='negative_votes',
        ),
        migrations.RemoveField(
            model_name='hotelingroup',
            name='positive_votes',
        ),
        migrations.RemoveField(
            model_name='hotelingroup',
            name='voters',
        ),
        migrations.AddField(
            model_name='hotelingroup',
            name='negative_voters',
            field=models.ManyToManyField(related_name='hotelingroup_negative_voters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hotelingroup',
            name='positive_voters',
            field=models.ManyToManyField(related_name='hotelingroup_positive_voters', to=settings.AUTH_USER_MODEL),
        ),
    ]
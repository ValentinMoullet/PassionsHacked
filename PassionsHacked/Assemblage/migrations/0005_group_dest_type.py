# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assemblage', '0004_auto_20161015_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='dest_type',
            field=models.CharField(default='city', max_length=50),
            preserve_default=False,
        ),
    ]

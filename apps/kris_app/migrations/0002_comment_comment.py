# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-24 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kris_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(default=True, max_length=1000),
            preserve_default=False,
        ),
    ]

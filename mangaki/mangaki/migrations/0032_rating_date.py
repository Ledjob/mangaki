# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-09 14:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mangaki', '0031_delete_deck'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='date',
            field=models.DateField(auto_now=True, default=datetime.datetime(2016, 4, 9, 14, 0, 22, 626332, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
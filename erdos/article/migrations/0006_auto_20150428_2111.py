# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20150428_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 21, 11, 41, 301143)),
        ),
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 21, 11, 41, 302094)),
        ),
    ]

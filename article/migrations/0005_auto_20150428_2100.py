# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20150428_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.TextField(default=b'Enter text here'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(default=b'Enter text here'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20150428_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='url',
        ),
        migrations.RemoveField(
            model_name='review',
            name='url',
        ),
    ]

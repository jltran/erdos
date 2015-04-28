# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20150428_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='editor',
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

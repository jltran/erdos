# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='decision',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=b'', unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='decision',
            field=models.NullBooleanField(),
        ),
    ]

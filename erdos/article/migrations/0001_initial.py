# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255)),
                ('author', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('editor', models.CharField(max_length=128)),
                ('active', models.BooleanField(default=True)),
                ('decision', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reviewer', models.CharField(max_length=128)),
                ('text', models.TextField()),
                ('url', models.URLField()),
                ('decision', models.BooleanField()),
                ('article', models.ForeignKey(to='article.Article')),
            ],
        ),
    ]

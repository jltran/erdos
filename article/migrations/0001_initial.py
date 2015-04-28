# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(default=b'Enter text here')),
                ('active', models.BooleanField(default=True)),
                ('decision', models.BooleanField()),
                ('author', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(default=b'Enter text here')),
                ('decision', models.BooleanField()),
                ('article', models.ForeignKey(to='article.Article')),
                ('reviewer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

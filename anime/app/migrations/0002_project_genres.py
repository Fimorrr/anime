# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='genres',
            field=models.ManyToManyField(to='app.Genre'),
        ),
    ]

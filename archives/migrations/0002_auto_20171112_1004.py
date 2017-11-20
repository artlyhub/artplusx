# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 10:04
from __future__ import unicode_literals

import archives.models
from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivepost',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=archives.models.scramble_uploaded_image),
        ),
    ]

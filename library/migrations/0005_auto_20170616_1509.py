# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-16 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_remove_mediainstance_late_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediainstance',
            name='due_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]

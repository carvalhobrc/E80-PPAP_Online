# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0002_certification_submission_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='submission_reason_other',
            field=models.CharField(default='', max_length=140),
        ),
    ]

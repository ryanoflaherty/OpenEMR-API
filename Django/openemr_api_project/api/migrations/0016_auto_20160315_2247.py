# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-15 22:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20160315_2247'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patientdata',
            options={'managed': True},
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-15 22:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_medicalhistory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patientdata',
            options={'managed': True},
        ),
    ]
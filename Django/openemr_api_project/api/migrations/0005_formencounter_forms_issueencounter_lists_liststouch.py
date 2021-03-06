# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_insurancedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormEncounter',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('facility', models.TextField(blank=True, null=True)),
                ('facility_id', models.IntegerField()),
                ('pid', models.BigIntegerField(blank=True, null=True)),
                ('encounter', models.BigIntegerField(blank=True, null=True)),
                ('onset_date', models.DateTimeField(blank=True, null=True)),
                ('sensitivity', models.CharField(blank=True, max_length=30, null=True)),
                ('billing_note', models.TextField(blank=True, null=True)),
                ('pc_catid', models.IntegerField()),
                ('last_level_billed', models.IntegerField()),
                ('last_level_closed', models.IntegerField()),
                ('last_stmt_date', models.DateField(blank=True, null=True)),
                ('stmt_count', models.IntegerField()),
                ('provider_id', models.IntegerField(blank=True, null=True)),
                ('supervisor_id', models.IntegerField(blank=True, null=True)),
                ('invoice_refno', models.CharField(max_length=31)),
                ('referral_source', models.CharField(max_length=31)),
                ('billing_facility', models.IntegerField()),
            ],
            options={
                'db_table': 'form_encounter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('encounter', models.BigIntegerField(blank=True, null=True)),
                ('form_name', models.TextField(blank=True, null=True)),
                ('form_id', models.BigIntegerField(blank=True, null=True)),
                ('pid', models.BigIntegerField(blank=True, null=True)),
                ('user', models.CharField(blank=True, max_length=255, null=True)),
                ('groupname', models.CharField(blank=True, max_length=255, null=True)),
                ('authorized', models.IntegerField(blank=True, null=True)),
                ('deleted', models.IntegerField()),
                ('formdir', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'forms',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IssueEncounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('list_id', models.IntegerField()),
                ('encounter', models.IntegerField()),
                ('resolved', models.IntegerField()),
            ],
            options={
                'db_table': 'issue_encounter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lists',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('begdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('returndate', models.DateField(blank=True, null=True)),
                ('occurrence', models.IntegerField(blank=True, null=True)),
                ('classification', models.IntegerField(blank=True, null=True)),
                ('referredby', models.CharField(blank=True, max_length=255, null=True)),
                ('extrainfo', models.CharField(blank=True, max_length=255, null=True)),
                ('diagnosis', models.CharField(blank=True, max_length=255, null=True)),
                ('activity', models.IntegerField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('pid', models.BigIntegerField(blank=True, null=True)),
                ('user', models.CharField(blank=True, max_length=255, null=True)),
                ('groupname', models.CharField(blank=True, max_length=255, null=True)),
                ('outcome', models.IntegerField()),
                ('destination', models.CharField(blank=True, max_length=255, null=True)),
                ('reinjury_id', models.BigIntegerField()),
                ('injury_part', models.CharField(max_length=31)),
                ('injury_type', models.CharField(max_length=31)),
                ('injury_grade', models.CharField(max_length=31)),
                ('reaction', models.CharField(max_length=255)),
                ('external_allergyid', models.IntegerField(blank=True, null=True)),
                ('erx_source', models.CharField(max_length=1)),
                ('erx_uploaded', models.CharField(max_length=1)),
                ('modifydate', models.DateTimeField()),
            ],
            options={
                'db_table': 'lists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ListsTouch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.BigIntegerField()),
                ('type', models.CharField(max_length=255)),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lists_touch',
                'managed': False,
            },
        ),
    ]

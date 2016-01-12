# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-12 13:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django_netjsonconfig.models.device
import jsonfield.fields
import model_utils.fields
import sortedm2m.fields
import uuid
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=63)),
                ('backend', models.CharField(choices=[('netjsonconfig.OpenWrt', 'OpenWRT'), ('netjsonconfig.OpenWisp', 'OpenWISP')], help_text='Select netjsonconfig backend', max_length=128, verbose_name='backend')),
                ('config', jsonfield.fields.JSONField(default=dict, help_text='configuration in NetJSON DeviceConfiguration format', verbose_name='configuration')),
                ('key', models.CharField(db_index=True, help_text='unique key that can be used to download the configuration', max_length=64, unique=True, default=django_netjsonconfig.models.device.get_random_key, validators=[django.core.validators.RegexValidator(re.compile(b'^[^\\s/\\.]+$'), code=b'invalid', message='Key must not contain spaces, dots or slashes.')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=63)),
                ('backend', models.CharField(choices=[('netjsonconfig.OpenWrt', 'OpenWRT'), ('netjsonconfig.OpenWisp', 'OpenWISP')], help_text='Select netjsonconfig backend', max_length=128, verbose_name='backend')),
                ('config', jsonfield.fields.JSONField(default=dict, help_text='configuration in NetJSON DeviceConfiguration format', verbose_name='configuration')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='device',
            name='templates',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text='configuration templates, applied fromfirst to last', to='django_netjsonconfig.Template', verbose_name='templates'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0062_auto_20160419_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='whiteboardmessage',
            name='category',
            field=models.CharField(choices=[('info', 'Info (light blue)'), ('warning', 'Warning (yellow)'), ('danger', 'Danger (red)'), ('success', 'Success (green)'), ('primary', 'Primary (dark blue)')], default='info', help_text='Category matches Bootstrap ones and defines color used for the message.', max_length=25, verbose_name='Category'),
        ),
    ]

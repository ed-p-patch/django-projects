# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-15 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0002_auto_20180515_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='ninja',
            name='f_name',
            field=models.CharField(default='0000000', max_length=255),
        ),
        migrations.AddField(
            model_name='ninja',
            name='l_name',
            field=models.CharField(default='0000000', max_length=255),
        ),
    ]

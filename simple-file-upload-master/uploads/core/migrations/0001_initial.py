# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-25 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(max_length=60)),
            ],
        ),
    ]

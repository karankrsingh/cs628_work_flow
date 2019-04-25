# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-25 14:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190425_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('teacher_comment', models.CharField(blank=True, max_length=255)),
                ('marks', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('report_meet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TeacherMeet')),
            ],
        ),
    ]
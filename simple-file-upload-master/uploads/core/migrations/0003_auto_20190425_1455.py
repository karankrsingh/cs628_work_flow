# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-25 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherMeet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_id', models.IntegerField()),
                ('schedule_date', models.DateTimeField()),
                ('future_work', models.CharField(max_length=250)),
                ('meet_student_roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Student')),
                ('meet_teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Teacher')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='teachermeet',
            unique_together=set([('week_id', 'meet_student_roll')]),
        ),
    ]
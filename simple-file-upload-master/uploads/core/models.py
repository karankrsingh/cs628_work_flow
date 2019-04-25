from __future__ import unicode_literals

from django.db import models



class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Teacher(models.Model):
    teacher_name=models.CharField(max_length=60,blank=False)

class Students(models.Model):
    std_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student_roll = models.CharField(max_length=60, primary_key=True)
    student_name = models.CharField(max_length=60, blank=False)
    topic = models.CharField(max_length=255, blank=False)

    
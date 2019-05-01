from __future__ import unicode_literals
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
# import composite_field

# class Document(models.Model):
#     description = models.CharField(max_length=255, blank=True)
#     document = models.FileField(upload_to='documents/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)


class Teacher(models.Model):
    teacher_id = models.IntegerField(default=1,primary_key=True)
    teacher_name = models.CharField(max_length=60, blank=False)

    def __str__(self):
        return str(self.teacher_id)+self.teacher_name


class Student(models.Model):
    std_teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student_roll = models.IntegerField(unique=True,primary_key=True)
    student_name = models.CharField(max_length=60, blank=False)
    topic = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return str(self.student_name) + str(self.student_roll)



class TeacherMeet(models.Model):
    week_id = models.IntegerField()
    meet_student_roll = models.ForeignKey(Student, on_delete=models.CASCADE)
    schedule_date = models.DateTimeField()
    future_work = models.CharField(max_length=250)

    # meet_id=models.CompositeField(week_id,meet_student_roll,primary_key=True)
    class Meta:
        unique_together = (("week_id", "meet_student_roll"),)

    def __str__(self):
        return str(self.week_id) + str(self.meet_student_roll)

class Report(models.Model):
    report_meet_id = models.ForeignKey(TeacherMeet, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)
    teacher_comment = models.CharField(max_length=255, blank=True,null=True)
    marks = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)],null=True,blank=True)

    def __str__(self):
        return str(self.report_meet_id) + str(self.document.name)

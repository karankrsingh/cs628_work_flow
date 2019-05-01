from django import forms

from .models import Report
from .models import TeacherMeet

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('description', 'document',)


class MeetingForm(forms.ModelForm):
    class Meta:
        model = TeacherMeet
        fields = ('schedule_date','future_work',)

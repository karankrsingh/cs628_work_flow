from django import forms

from .models import Report


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('description', 'document',)

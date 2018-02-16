from django import forms
from .models import Student

class createFrom(forms.ModelForm):
    class Meta:
        model=Student
        fields=[
            'name',
            'roll',
            'dept',
            'email'
        ]
from django import forms
from django.core import validators

from .models import Question360


class Question360Form(forms.ModelForm):

    class Meta:
        model = Question360
        fields = ('question',
                  'ranks',
                  'ability')
        widgets = {
            'question': forms.TextInput(),
            'ranks': forms.CheckboxSelectMultiple(),
            'ability': forms.Select()
        }

from django import forms

from .models import Seamans


class SeamanForm(forms.ModelForm):

    class Meta:
        model = Seamans
        fields = ('last_name', 'first_name')
        widgets = {
            'last_name': forms.TextInput(),
            'first_name': forms.TextInput(),
        }

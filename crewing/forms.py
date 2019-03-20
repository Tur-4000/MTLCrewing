from django import forms

from .models import Seamans


class SeamanForm(forms.ModelForm):

    class Meta:
        model = Seamans
        fields = ('last_name_en', 'first_name_en',
                  'last_name_ru', 'first_name_ru',
                  'last_name_ua', 'first_name_ua',)
        widgets = {
            'last_name_en': forms.TextInput(),
            'first_name_en': forms.TextInput(),
            'last_name_ru': forms.TextInput(),
            'first_name_ru': forms.TextInput(),
            'last_name_ua': forms.TextInput(),
            'first_name_ua': forms.TextInput(),
        }

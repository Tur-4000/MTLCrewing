from django import forms

from .models import Seamans, Ranks, Vessels


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


class RankForm(forms.ModelForm):

    class Meta:
        model = Ranks
        fields = ('rank_title',)
        widgets = {
            'rank_title': forms.TextInput(),
        }


class VesselForm(forms.ModelForm):

    class Meta:
        model = Vessels
        fields = ('vessel_name', 'vessel_type', 'dwt')
        widgets = {
            'vessel_name': forms.TextInput(),
            'vessel_type': forms.TextInput(),
            'dwt': forms.NumberInput,
        }

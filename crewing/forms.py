from django import forms
from django.core import validators

from .models import Seamans, Ranks, Vessels, Contracts


class SeamanForm(forms.ModelForm):
    foto = forms.ImageField(label='Фото',
                            validators=[validators.FileExtensionValidator(
                                allowed_extensions=('jpg', 'png'))],
                            error_messages={'invalid_extension': 'Этот формат '
                                            + 'файлов не поддерживается'},
                            required=False)
    last_name_en = forms.TextInput()
    first_name_en = forms.TextInput()
    last_name_ru = forms.TextInput()
    first_name_ru = forms.TextInput()
    last_name_ua = forms.TextInput()
    first_name_ua = forms.TextInput()

    class Meta:
        model = Seamans
        fields = ('last_name_ru', 'first_name_ru',
                  'last_name_en', 'first_name_en',
                  'last_name_ua', 'first_name_ua',
                  'foto')


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


class ContractForm(forms.ModelForm):
    vessel = forms.Select()
    rank = forms.Select()
    sign_in_date = forms.TextInput()
    sign_off_date = forms.TextInput()

    class Meta:
        model = Contracts
        fields = ('vessel', 'rank', 'sign_in_date', 'sign_off_date')
        # widgets = {
        #     'vessel': forms.Select(),
        #     'rank': forms.Select(),
        #     'sign_in_date': forms.DateInput(attrs={'type': 'date'}),
        #     'sign_off_date': forms.DateInput(attrs={'type': 'date'})
        # }

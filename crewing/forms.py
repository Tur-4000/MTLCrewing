from django import forms

from .models import Seamans, Ranks, Vessels, Opinions, Contracts, \
    Seaman360Question


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


class OpinionForm(forms.ModelForm):

    class Meta:
        model = Opinions
        fields = ('date', 'contract', 'author', 'opinion_text')
        widgets = {
            'date': forms.TextInput(attrs={'class': 'span2', 'id': 'dp1'}),
            'contract': forms.Select(),
            'author': forms.TextInput(),
            'opinion_text': forms.Textarea(attrs={'rows': 3})
        }


class ContractForm(forms.ModelForm):

    class Meta:
        model = Contracts
        fields = ('vessel', 'rank', 'sign_in_date', 'sign_off_date')
        widgets = {
            'vessel': forms.Select(),
            'rank': forms.Select(),
            'sign_in_date': forms.DateInput(attrs={'type': 'date'}),
            'sign_off_date': forms.DateInput(attrs={'type': 'date'})
        }


class Seaman360QuestionForm(forms.ModelForm):

    class Meta:
        model = Seaman360Question
        fields = ('question', 'rank', 'ability')
        widgets = {
            'question': forms.TextInput(),
            'rank': forms.CheckboxSelectMultiple(),
            'ability': forms.Select()
        }

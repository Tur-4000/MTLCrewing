from django import forms
from django.forms import modelformset_factory
from django.core import validators

from .models import Question360, Ability360, Scoring360SeamanAbility
from crewing.models import Ranks


class Question360Form(forms.ModelForm):
    question = forms.CharField(max_length=128, label='Вопрос')
    ability = forms.ModelChoiceField(queryset=Ability360.objects.all(),
                                     label='Компетенция',
                                     help_text='Не забудьте выбрать компетенцию',
                                     widget=forms.Select())
    ranks = forms.ModelMultipleChoiceField(queryset=Ranks.objects.all(),
                                           label='Должности',
                                           widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Question360
        fields = ('question', 'ability', 'ranks')


class Scoring360Form(forms.ModelForm):

    class Meta:
        model = Scoring360SeamanAbility
        fields = ('date', 'appraiser')


Scoring360FormSet = modelformset_factory(Scoring360SeamanAbility,
                                         fields=('ability', 'ability_value'))

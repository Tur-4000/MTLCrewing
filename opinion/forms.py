from django import forms
from django.core import validators

from crewing.models import Contracts
from .models import Opinion


class OpinionForm(forms.ModelForm):
    date = forms.TextInput(attrs={'class': 'span2', 'id': 'dp1'})
    contract = forms.ModelChoiceField(queryset=Contracts.objects.none())
    author = forms.TextInput()
    opinion_text = forms.Textarea(attrs={'rows': 3})
    opinion_file = forms.FileField(
        label='Файл',
        validators=[validators.FileExtensionValidator(
            allowed_extensions=('jpg', 'png', 'pdf', 'doc', 'docx', 'odt'))],
        error_messages={'invalid_extension': 'Этот формат '
                                             + 'файлов не поддерживается'},
        required=False)

    class Meta:
        model = Opinion
        fields = ('date', 'contract', 'author', 'opinion_text', 'opinion_file')
        # required = ('date', 'author', 'opinion_text') # не сработало

    def __init__(self, *args, **kwargs):
        if 'contracts' in kwargs:
            qs = kwargs.pop('contracts')
        else:
            qs = None

        super(OpinionForm, self).__init__(*args, **kwargs)

        try:
            self.fields['contract'].queryset = qs
            self.fields['contract'].required = False
        except AttributeError:
            pass

from django import forms
from django.core.validators import RegexValidator
from .models import *
import re

class RegisterDjangoModel(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    pno = forms.CharField(max_length=50, required=False, validators=[RegexValidator('\+91\s?[6-9]\d{9}')])
    email = forms.EmailField(required=False)
    add = forms.CharField(max_length=50, required=False)
    username=forms.CharField(max_length=50, required=False)
    password = forms.CharField(max_length=50, required=False)


class RegisterModelForm(forms.ModelForm):
    class Meta:
        model=Register
        fields='__all__'

    def clean_pno(self):
        pno = self.cleaned_data['pno']
        if re.match('\+91\s?[6-9]\d{9}', pno):
            return pno
        return None
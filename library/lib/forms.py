from django import forms
from .models import *


class bask(forms.ModelForm):
    class Meta:
        model = client
        fields = ['name', 'phone']





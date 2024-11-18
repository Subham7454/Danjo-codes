from django import forms
from .models import ChaiVriety

class ChaiVarietyForm(forms.Form):
    chai_varity=forms.ModelChoiceField(queryset=ChaiVriety.objects.all(),label="select chai variety")#this will create a dropdown because i ASKED for it
    
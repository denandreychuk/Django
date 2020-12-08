from django import forms
from .models import CustomerApp

class CustomerAppForm(forms.Form):
    name = forms.CharField(required=True)
    token = forms.CharField(max_length=20)
    client = forms.CharField(max_length=20)
    status = forms.ChoiceField(widget=forms.Select, choices=CustomerApp.Status.choices)
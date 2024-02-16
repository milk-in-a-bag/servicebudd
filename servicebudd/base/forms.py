from django import forms

class ServiceProvidersNameFilterForm(forms.Form):
    name = forms.CharField()
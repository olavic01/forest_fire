from django import forms

class FireRiskForm(forms.Form):
    FFMC = forms.FloatField(label='FFMC Index')
    DMC = forms.FloatField(label='DMC Index')
    DC = forms.FloatField(label='DC Index')
    ISI = forms.FloatField(label='ISI Index')

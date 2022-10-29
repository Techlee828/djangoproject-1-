from django import forms



class ManualForm(forms.Form):
    title = forms.CharField()
    body = forms.BooleanField()

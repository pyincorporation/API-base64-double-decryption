from django import forms

class Form(forms.Form):
    username = forms.CharField(widget=forms.TextInput({'placeholder':'username'}))
    password = forms.CharField(widget=forms.TextInput({'placeholder':'********'}))
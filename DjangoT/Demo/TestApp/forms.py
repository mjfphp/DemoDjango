from django import forms

class UserRegistrar(forms.Form):
    fname = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    lname = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}  ))
    age = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}  ))
    dn = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}  ))

class CryptMsg(forms.Form):
    Msg = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    Cle = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))


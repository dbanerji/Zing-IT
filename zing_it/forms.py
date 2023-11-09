from django import forms

class Signup(forms.Form):
    full_name = forms.CharField(required=True,max_length=50)
    email = forms.CharField(required=True,max_length=50)
    password = forms.CharField(widget=forms.PasswordInput,required=True,min_length=5)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True, min_length=5)
    
class Login(forms.Form):
    email = forms.CharField(required=True,max_length=50)
    password = forms.CharField(widget=forms.PasswordInput,required=True, min_length=5)
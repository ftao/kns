from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.Form):
    username = forms.CharField(max_length = 30, required = True)
    password = forms.CharField(widget = forms.PasswordInput(), required = True)
    email = forms.EmailField(required = True)
    
    def clean_username(self): 
        try:
            User.objects.get(username = self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError('username already in use')

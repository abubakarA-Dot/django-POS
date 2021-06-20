from django import forms
from django.forms import TextInput, Select, FileInput, CheckboxInput, EmailInput, NumberInput, PasswordInput, IntegerField
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    phn_number = forms.IntegerField()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'phn_number',
                  'last_name']


class UpdateUserForm(forms.ModelForm):
    phn_number = forms.IntegerField()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'phn_number', 
                  'last_name']

        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Your Username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Enter email address'}),
            'phn_number': IntegerField(),
            'first_name': TextInput(attrs={'class': 'form-control', 'id': 'first_name', 'placeholder': 'Your First Name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'id': 'last_name', 'placeholder': 'Your Last Name'}),
            'password1': PasswordInput(attrs={'class': 'form-control', 'id': 'password1', 'placeholder': 'Your password1'}),
            'password2': PasswordInput(attrs={'class': 'form-control', 'id': 'password2', 'placeholder': 'Your password2'}),
        }
        

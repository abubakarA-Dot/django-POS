from django import forms
from django.forms import TextInput, Select, FileInput, CheckboxInput, EmailInput, NumberInput
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 
                  'last_name']

        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Your Username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Enter email address'}),
            'phn_number': NumberInput(attrs={'class': 'form-control', 'id': 'phn_number', 'placeholder': '123456789'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'id': 'first_name', 'placeholder': 'Your First Name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'id': 'last_name', 'placeholder': 'Your Last Name'}),
        }
        

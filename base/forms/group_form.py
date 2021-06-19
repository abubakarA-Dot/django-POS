from django.contrib.auth.models import Group, Permission
from django import forms


class UpdateGroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = '__all__'

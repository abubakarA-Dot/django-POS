from django import forms
from django.forms import TextInput, Select, FileInput, CheckboxInput
from base.models.category import Category


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name',  'status', 'parent']

        # widgets = {
        #     'name': TextInput(attrs={'class': 'form-control', 'id': 'name'}),
        #     'parent': Select(attrs={'class': 'form-control'}),
        #     'category_image': FileInput(attrs={'class': 'form-control', 'id': 'imageUpload'}),
        #     'is_active': CheckboxInput(attrs={'class': 'checkbox', 'id': 'activity'})
        # }


class UpdateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name',  'status', 'parent']

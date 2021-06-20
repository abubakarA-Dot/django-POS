from django import forms
from django.forms import TextInput, Select, FileInput, NumberInput, Textarea

from base.models.product import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_uuid', 'product_name',  'Price', 'expiry_date',
                  'manufactor_date', 'category_id', 'description', 'stock', 'count_sold']
        # widgets = {
        #     'product_name': TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Enter Product Name'}),
        #     'product_category': Select(attrs={'class': 'form-control', 'id': 'product_category'}),
        #     'price': NumberInput(attrs={'class': 'form-control', 'id': 'price'}),
        #     'description': Textarea(attrs={'class': 'form-control', 'id': 'description', 'placeholder': "Your Product's history here"}),
        #     'product_image': FileInput(attrs={'class': 'form-control', 'id': 'product_image'}),
        # }
class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_uuid', 'product_name', 'Quantity', 'Price', 'expiry_date',
                  'manufactor_date', 'category_id', 'description', 'stock', 'count_sold']

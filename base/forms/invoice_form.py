from base.models import product
from base.models.product import Product
from base.models.order import OrderItem
from django import forms
from django.db.models.fields import DateField
from django.forms import TextInput, Select, FileInput, NumberInput, Textarea, SelectMultiple
from django.forms.widgets import DateInput

from base.models.Invoice import Invoice


class InvoiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].queryset = Product.objects.only('Price').get(product_name="HP")

    class Meta:
        model = Invoice
        fields = '__all__'
        widgets = {
            'Product_id': Select(attrs={'class': 'form-control', 'id': 'product_name'}),
            'Event_Name': Select(attrs={'class': 'form-control', }),
            'sold_Quantity': NumberInput(attrs={'class': 'form-control', 'id': 'qty'}),
            'price': TextInput(attrs={'class': 'form-control', 'id': 'price'}),
            'total_price': TextInput(attrs={'class': 'form-control', 'id': 'total_price'}),
            'date_time': DateInput(attrs={'class': 'form-control',}),
        }


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['orderItem'].widget.attrs['hidden'] = True

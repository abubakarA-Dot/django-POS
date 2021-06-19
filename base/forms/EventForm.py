from django import forms
from django.forms import TextInput, Select, FileInput, CheckboxInput
from base.models.Invoice import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'event_name': Select(attrs={'class': 'form-control'}),
        }

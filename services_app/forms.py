from django import forms
from django.forms.widgets import NumberInput
from services_app.models import Visa


class VisaForm(forms.ModelForm):
    # email = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter Your Email'}), label="")
    # name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter Your Number'}), label="")
    date_of_birth = forms.DateField(widget = NumberInput(attrs={'type': 'date'}))
    

    class Meta:
        model = Visa
        fields = ['where_from', 'where_going', 'visa_type', 'which_country_passport', 'name', 'email', 'mobile', 'passport_number', 'nid_number', 'occupation', 'gender', 'date_of_birth']
        # fields = '__all__'

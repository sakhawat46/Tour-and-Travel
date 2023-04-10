from django import forms
from django.forms.widgets import NumberInput, TextInput, EmailInput
from services_app.models import Visa, Passport


class VisaForm(forms.ModelForm):
    # email = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter Your Email'}), label="")
    # name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter Your Number'}), label="")
    date_of_birth = forms.DateField(widget = NumberInput(attrs={'type': 'date'}))
    

    class Meta:
        model = Visa
        fields = ['where_from', 'where_going', 'visa_type', 'which_country_passport', 'name', 'email', 'mobile', 'passport_number', 'nid_number', 'occupation', 'gender', 'date_of_birth']
        # fields = '__all__'




class PassportForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget = NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = Passport
        fields = '__all__'

        # widgets = {
        #     'full_name': TextInput(attrs={
        #         'class': "form-control",
        #         'style': 'max-width: 700px; height: 100px;',
        #         'placeholder': 'Name'
        #         }),
        #     'email': EmailInput(attrs={
        #         'class': "form-control", 
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Email'
        #         })
        # }
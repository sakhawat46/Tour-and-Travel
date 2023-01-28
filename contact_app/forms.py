from django import forms
from contact_app.models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter Your Name'}), label="Name")
    email = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter Your Email'}), label="")
    mobile_number = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter Mobile Number'}), label="")
    subject = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter Your Subject'}), label="")

    class Meta:
        model = Contact
        fields = ['name', 'email', 'mobile_number', 'subject', 'message']
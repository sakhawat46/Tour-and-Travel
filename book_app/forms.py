from django import forms
from book_app.models import Book


class BookForm(forms.ModelForm):
    arrivals = forms.DateField(widget = forms.TextInput(attrs = {'type':'date'}), label="")
    leaving = forms.DateField(widget = forms.TextInput(attrs = {'type':'date'}), label="")
    name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter Your Name'}), label="")
    mobile_number = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter Mobile Number'}), label="")
    # tour_place = forms.CharField(widget = forms.TextInput(attrs={}),label="")
    # tour_place = forms.ModelChoiceField(queryset=Book.objects.all())

    class Meta:
        model = Book
        fields = ['tour_place', 'name', 'mobile_number', 'arrivals', 'leaving']
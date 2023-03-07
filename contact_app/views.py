from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages

# Create your views here.
from django.urls import reverse, reverse_lazy
from contact_app.forms import ContactForm

def contact(request):
    form = ContactForm()
    registered = False
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
            
            form = ContactForm()

            # messages.success(request, "Booking Successfully!")
            # return HttpResponseRedirect(reverse('contact_app:contact'))
    diction = {'form':form, 'registered':registered}
    return render(request,'contact_app/contact.html', context = diction)
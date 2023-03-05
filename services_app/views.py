from django.shortcuts import render, HttpResponseRedirect, redirect

from django.urls import reverse, reverse_lazy
from services_app.forms import VisaForm

# Create your views here.

def services(request):

    return render(request,'services_app/services.html')


def visa(request):
    form = VisaForm()
    if request.method == "POST":
        form = VisaForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('services_app:services'))
    diction = {'form':form}
    return render(request,'services_app/visa.html', context = diction)


def visa_details(request):
    form = VisaForm()
    if request.method == "POST":
        form = VisaForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('services_app:services'))
    diction = {'form':form}
    return render(request,'services_app/visa_details.html', context = diction)



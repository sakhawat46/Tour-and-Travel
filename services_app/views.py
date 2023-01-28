from django.shortcuts import render, HttpResponseRedirect, redirect

# Create your views here.

def services(request):

    return render(request,'services_app/services.html')
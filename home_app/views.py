from django.shortcuts import render, HttpResponseRedirect, redirect
from home_app.models import Home

# Create your views here.

def home(request):
    # home = Home.objects.all().order_by('-id')
    # home = Home.objects.filter(video_title__in=[0])
    # home = Home.objects.filter()[:1].get()
    
    home = Home.objects.first()
    diction = {'home':home}
    return render(request,'home_app/home.html', context = diction)
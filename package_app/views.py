from django.shortcuts import render, HttpResponseRedirect, redirect
from package_app.models import Packages

# Create your views here.

def package(request):
    packages = Packages.objects.all().order_by('-id')
    diction = {'packages' : packages}
    return render(request,'package_app/package.html', context = diction)



def package_details(request, slug):

    # access package without loop in template
    package = Packages.objects.get(slug=slug)

    # access package using loop in template
    packages = Packages.objects.filter(slug=slug).order_by('-id')

    return render(request, 'package_app/package_details.html', context={'package':package, 'packages':packages})
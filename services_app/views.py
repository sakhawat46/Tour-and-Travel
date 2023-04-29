from django.shortcuts import render, HttpResponseRedirect, redirect

from django.urls import reverse, reverse_lazy
from services_app.forms import VisaForm, PassportForm
from services_app.models import Country, Flight, Popular_Destination

from django.contrib import messages

# Create your views here.

def services(request):

    return render(request,'services_app/services.html')


def visa(request):
    form = VisaForm()
    registered = False
    all_country = Country.objects.all().order_by('-id')
    popular_destination = Popular_Destination.objects.all().order_by('-id')
    if request.method == "POST":
        form = VisaForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
            form = VisaForm()
            # return HttpResponseRedirect(reverse('services_app:services'))
    diction = {'form':form, 'all_country':all_country, 'registered':registered, 'popular_destination':popular_destination}
    return render(request,'services_app/visa.html', context = diction)


def destination_details(request, slug):

    # access country without loop in template
    destination = Popular_Destination.objects.get(slug=slug)

    diction = {'destination':destination}

    return render(request, 'services_app/popular_desti_details.html', context = diction)


def country_details(request, slug):

    # access country without loop in template
    country = Country.objects.get(slug=slug)

    diction = {'country':country}

    return render(request, 'services_app/country_details.html', context = diction)


def flight(request):
    if request.method == 'POST':
        flight_type = request.POST.get('flight_type')
        flying_from = request.POST.get('flying_from')
        flying_to = request.POST.get('flying_to')
        departing = request.POST.get('departing')
        returning = request.POST.get('returning')
        adults = request.POST.get('adults')
        children = request.POST.get('children')
        travel_class = request.POST.get('travel_class')

        form = Flight(
            flight_type = flight_type,
            flying_from = flying_from,
            flying_to = flying_to,
            departing = departing,
            returning = returning,
            adults = adults,
            children = children,
            travel_class = travel_class
        )

        form.save()

        messages.success(request, "Flight Booking Successfully.")
        return redirect('services_app:flight')

    return render(request,'services_app/flight.html')


def passport(request):
    form = PassportForm()
    registered = False
    if request.method == "POST":
        form = PassportForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
            form = PassportForm()
            # return HttpResponseRedirect(reverse('services_app:passport'))
    diction = {'form':form, 'registered': registered}
    return render(request,'services_app/passport.html', context = diction)




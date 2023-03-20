from django.shortcuts import render, HttpResponseRedirect, redirect

from django.urls import reverse, reverse_lazy
from services_app.forms import VisaForm
from services_app.models import Country, Flight

from django.contrib import messages

# Create your views here.

def services(request):

    return render(request,'services_app/services.html')


def visa(request):
    form = VisaForm()
    all_country = Country.objects.all().order_by('-id')
    if request.method == "POST":
        form = VisaForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('services_app:services'))
    diction = {'form':form, 'all_country':all_country}
    return render(request,'services_app/visa.html', context = diction)



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


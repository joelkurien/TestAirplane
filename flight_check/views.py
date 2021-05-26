from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import FlightDetails, PassengerDetails
# Create your views here.
def index(request):
    return render(request, "flight_check/index.html", {
        "flights": FlightDetails.objects.all()
    })

def flight(request, flight_id):
    flight = FlightDetails.objects.get(pk=flight_id)
    return render(request, "flight_check/flights.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": PassengerDetails.objects.exclude(flights = flight).all()
    })

def book(request, flight_id):
    #check if the request is a post request
    if request.method == 'POST':
        print(request.POST)
        flight = FlightDetails.objects.get(pk=flight_id)
        #it finds all the passengers with a particular passenger id
        passenger = PassengerDetails.objects.get(pk=request.POST['passenger'])
        passenger.flights.add(flight) # it finds all the flight a particular passenger takes

        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))

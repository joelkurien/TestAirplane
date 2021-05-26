from django.contrib import admin

from .models import FlightDetails, AirportDetails, PassengerDetails
# Register your models here.
admin.site.register(AirportDetails)
admin.site.register(FlightDetails)
admin.site.register(PassengerDetails)

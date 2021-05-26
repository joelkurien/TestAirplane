from django.db import models

# Create your models here.
class AirportDetails(models.Model):
    code = models.CharField(max_length=5)
    city = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.city} ({self.code})"

class FlightDetails(models.Model):
    start_location = models.ForeignKey(AirportDetails, on_delete=models.CASCADE, related_name="departures")
    end_location = models.ForeignKey(AirportDetails, on_delete=models.CASCADE, related_name='arrival')
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.start_location} to {self.end_location} in {self.duration}"

    def is_valid_flight(self):
        return self.start_location != self.end_location and self.duration > 0

class PassengerDetails(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    flights = models.ManyToManyField(FlightDetails, blank=True, related_name='passengers')

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

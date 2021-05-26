from django.test import Client, TestCase

from .models import AirportDetails, FlightDetails, PassengerDetails
# Create your tests here.
class Test(TestCase):
        def setUp(self):
            a1 = AirportDetails.objects.create(code='CCC', city='City C')
            a2 = AirportDetails.objects.create(code='DDD', city='City D')

            f1 = FlightDetails.objects.create(start_location=a1, end_location=a2, duration=200)
            f2 = FlightDetails.objects.create(start_location=a1, end_location=a1, duration=300)
            f3 = FlightDetails.objects.create(start_location=a1, end_location=a2, duration=-299)

        def test_departure_count(self):
            a = AirportDetails.objects.get(code='CCC')
            self.assertEqual(a.departures.count(), 3)

        def test_arrival_count(self):
            a = AirportDetails.objects.get(code='CCC')
            self.assertEqual(a.arrival.count(), 1)

        def test_valid_flight(self):
            a = AirportDetails.objects.get(code='CCC')
            b = AirportDetails.objects.get(code='DDD')
            f = FlightDetails.objects.get(start_location=a, end_location=b, duration=200)
            self.assertTrue(f.is_valid_flight())

        def test_invalid_flight(self):
            a = AirportDetails.objects.get(code='CCC')
            f = FlightDetails.objects.get(start_location=a, end_location=a)
            self.assertFalse(f.is_valid_flight())

        def test_invalid_duration(self):
            a = AirportDetails.objects.get(code='CCC')
            b = AirportDetails.objects.get(code='DDD')
            f = FlightDetails.objects.get(start_location=a, end_location=b, duration=-299)
            self.assertFalse(f.is_valid_flight())

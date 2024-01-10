# from django.db import models
# from apps.common.models import BaseModel
#
#
# class Flight(BaseModel):
#     airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
#     flight_number = models.CharField(max_length=10)
#     departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_airport')
#     arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_airport')
#     departure_time = models.DateTimeField()
#     arrival_time = models.DateTimeField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)

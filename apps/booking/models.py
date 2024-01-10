# from django.db import models
#
# # Create your models here.
# from apps.common.models import BaseModel
#
#
# class Booking(BaseModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
#     departure_date = models.DateField()
#     return_date = models.DateField(null=True, blank=True)
#     passengers = models.PositiveIntegerField()
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     is_paid = models.BooleanField(default=False)

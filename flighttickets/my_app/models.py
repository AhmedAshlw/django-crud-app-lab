from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Flight(models.Model):
    departure = models.DateField()
    sourcePlace = models.CharField(max_length=100)
    destinationPlace = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.departure.strftime("%Y-%m-%d")

    def get_absolute_url(self):
        return reverse("flight-detail", kwargs={"flight_id": self.id})

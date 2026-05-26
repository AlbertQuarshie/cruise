from django.db import models
from django.contrib.auth.models import User

class Cruise(models.Model):
    name = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    departure_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} to {self.destination}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cruise = models.ForeignKey(Cruise, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    number_of_tickets = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.cruise.name}"
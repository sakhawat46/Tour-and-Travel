from django.db import models
from package_app.models import Packages
# Create your models here.

class Book(models.Model):
    tour_place = models.ForeignKey(Packages, on_delete=models.CASCADE, verbose_name='Tour Place')
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    arrivals = models.DateField()
    leaving = models.DateField()

    def __str__(self):
        return str(self.tour_place)
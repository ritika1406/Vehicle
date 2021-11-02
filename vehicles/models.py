from django.db import models
from django.urls import reverse

# Create your models here.
class Vehicledata(models.Model):
    vehiclenumber= models.CharField(max_length=50)
    Averagespeed = models.IntegerField()
    Enginestatus = models.IntegerField()
    FuelLevel = models.IntegerField()
    Temperature = models.IntegerField()
    def __str__(self):
        return str(self.vehiclenumber)
    # def get_absolute_url(self):
    #     return reverse("Vehicledata :Vehicledata ", kwargs={"id": self.id})



    
    
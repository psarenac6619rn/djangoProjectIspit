from django.db import models

# Create your models here.


class Drvo(models.Model):
    vrsta_Drveta = models.CharField(max_length=50)
    metar = models.CharField(max_length=4)
    cena_DIN = models.IntegerField(default=0)

    def __str__(self):
        return self.naziv

class Stolica(models.Model):
    model = models.CharField(max_length=100)
    dimenzije = models.CharField(max_length=50)
    cena_DIN = models.IntegerField(default=0)
    tip_Drveta = models.ForeignKey(Drvo, on_delete = models.CASCADE)

    def __str__(self):
        return self.model
from django.db import models

# Create your models here.


class Drvo(models.Model):
    vrsta = models.CharField(max_length=50)
    cena_DIN = models.IntegerField(default=0)

    def __str__(self):
        return self.vrsta

class Stolica(models.Model):
    model = models.CharField(max_length=100)
    dimenzije = models.CharField(max_length=50)
    cena_DIN = models.IntegerField(default=0)
    proizvedeno_Od = models.ForeignKey(Drvo, on_delete = models.CASCADE)

    def __str__(self):
        return self.model
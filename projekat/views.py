from django.shortcuts import render
from .models import *


def stolica(request):
    drvo = Drvo.objects.all()
    total_drvo = drvo.count()
    cena = Drvo.objects.filter(cena_DIN=50).count()
    stolica = Stolica.objects.all()
    return render(request, 'stolica/dashboard.html', {'stolica': stolica, 'drvo': drvo , 'total_drvo': total_drvo, 'cena':cena})








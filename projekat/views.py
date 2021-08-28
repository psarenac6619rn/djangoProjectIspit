from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def stolica(request):
    drvo = Drvo.objects.all()
    total_drvo = drvo.count()
    cena = Drvo.objects.filter(cena_DIN=500).count()
    stolica = Stolica.objects.all()
    total_stolica = stolica.count
    return render(request, 'stolica/dashboard.html', {'stolica': stolica, 'drvo': drvo , 'total_drvo': total_drvo, 'cena':cena , 'total_stolica':total_stolica})

def user(request):
    user = User.objects.all()
    total_users = user.count()
    brojac = 0
    for u in User.objects.all():
        if '@gmail.com' in u.email:
            brojac = brojac+1
    email = brojac
    return render(request, 'stolica/user.html', {'user': user, 'total_users':total_users, 'email':email})






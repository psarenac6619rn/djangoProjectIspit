from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .decorators import unauthentificated_user, allow_users, admin_only
from .forms import *

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .models import *

@unauthentificated_user
def registerPage(request):
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name='customer')
                user.groups.add(group)

                messages.success(request, 'Account created for ' + username)

                return redirect('projekat:login')

        context = {'form':form}
        return render(request, 'stolica/register.html', context)

@unauthentificated_user
def loginPage(request):
        if request.method == 'POST':
           username = request.POST.get('username')
           password = request.POST.get('password')

           user = authenticate(request, username=username, password=password)

           if user is not None:
               login(request, user)
               return redirect('stolica:home')
           else:
               messages.info(request, 'Username or Password is incorect')

        context = {}
        return render(request, 'stolica/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('projekat:login')

@login_required(login_url='stolica:login')
@admin_only
def stolica(request):
    drvo = Drvo.objects.all()
    stolica = Stolica.objects.all()
    return render(request, 'stolica/dashboard.html', {'stolica': stolica, 'drvo': drvo})

def userPage(request):
    drvo = Drvo.objects.all()
    stolica = Stolica.objects.all()
    return render(request, 'stolica/user.html', {'stolica': stolica, 'drvo': drvo})

@login_required(login_url='stolica:login')
@allow_users(allowed_roles=['admin'])
def createDrvo(request):
    form = DrvoForm()
    if request.method == 'POST':
        form = DrvoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(ValueError)

    context = {'form': form}

    return render(request, 'stolica/drvo.html', context)

@login_required(login_url='stolica:login')
@allow_users(allowed_roles=['admin'])
def createStolica(request):

    form = StolicaForm()
    if request.method == 'POST':
        form = StolicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(ValueError)

    context = {'form':form}

    return render(request, 'stolica/stolica.html', context)

@login_required(login_url='stolica:login')
@allow_users(allowed_roles=['admin'])
def updateDrvo(request, drvo_id):

    drvo = Drvo.objects.get(id = drvo_id)
    form = DrvoForm(instance=drvo)
    if request.method == "POST":
        form = DrvoForm(request.POST, instance=drvo)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(ValueError)


    context = {'form':form}
    return render(request, 'stolica/drvo.html', context)

@login_required(login_url='stolica:login')
@allow_users(allowed_roles=['admin'])
def updateStolica(request, stolica_id):

    stolica = Stolica.objects.get(id = stolica_id)
    form = StolicaForm(instance=stolica)
    if request.method == "POST":
        form = StolicaForm(request.POST, instance=stolica)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(ValueError)


    context = {'form':form}
    return render(request, 'stolica/stolica.html', context)

@login_required(login_url='stolica:login')
@allow_users(allowed_roles=['admin'])
def deleteDrvo(request, drvo_id):
    drvo = Drvo.objects.get(id=drvo_id)
    if request.method == "POST":
        drvo.delete()
        return redirect('/')

    context = {'item': drvo}
    return  render(request, 'stolica/delete_drvo.html', context)

@login_required(login_url='stolica:login')
@allow_users(allowed_roles=['admin'])
def deleteStolica(request, stolica_id):

    stolica = Stolica.objects.get(id=stolica_id)

    if request.method == "POST":
        stolica.delete()
        return redirect('/')

    context = {'item': stolica}
    return  render(request, 'stolica/delete_stolica.html', context)
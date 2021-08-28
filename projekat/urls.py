from django.urls import path
from . import views

app_name = 'projekat'

urlpatterns = [

    path('', views.stolica, name='home')



]

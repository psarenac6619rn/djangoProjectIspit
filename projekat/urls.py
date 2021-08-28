from django.urls import path
from . import views

app_name = 'projekat'

urlpatterns = [

    path('', views.stolica, name='stolicaView'),
    path('user', views.user, name='userPage')


]

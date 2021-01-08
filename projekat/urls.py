from django.urls import path
from . import views

app_name = 'projekat'

urlpatterns = [

    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.stolica, name='home'),
    path('user', views.userPage, name='userPage'),

    path('stolica', views.createStolica, name='stolica'),
    path('drvo', views.createDrvo, name='drvo'),

    path('update_drvo/<int:drvo_id>/', views.updateDrvo, name='UpdateD'),
    path('update_stolica/<int:stolica_id>/', views.updateStolica, name='UpdateS'),

    path('deleteDrvo/<int:drvo_id>/', views.deleteDrvo, name='DeleteD'),
    path('deleteStolica/<int:stolica_id>/', views.deleteStolica, name='DeleteS')

]

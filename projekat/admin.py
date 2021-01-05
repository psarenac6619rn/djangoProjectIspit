from django.contrib import admin

# Register your models here.
from .models import Drvo, Stolica

admin.site.register(Drvo)
admin.site.register(Stolica)
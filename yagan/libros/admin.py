from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import Libro

admin.site.register(Session)
admin.site.register(Libro)
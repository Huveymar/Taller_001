from django.contrib import admin

# Register your models here.

from .models import Proyecto, Tarea, Usuario

admin.site.register(Proyecto)
admin.site.register(Tarea)
admin.site.register(Usuario)

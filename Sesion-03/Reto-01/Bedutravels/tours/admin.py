from django.contrib import admin
from .models import User, Zona

# Personalizando modelos en el admin
class UserAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "nombre", "apellidos", "email", "fechaNacimiento",
        "genero", "tipo")


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Zona)

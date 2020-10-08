from django.contrib import admin
from .models import User, Zona, Tour, Opinion, Salida

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "nombre", "apellidos", "email", "genero",
        "fechaNacimiento", "tipo")
admin.site.register(User, UserAdmin)

class ZonaAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "nombre", "descripcion", "latitud", "longitud")
admin.site.register(Zona, ZonaAdmin)

class TourAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "nombre", "slug", "operador", "tipoDeTour",
        "descripcion", "pais", "zonaSalida", "zonaLlegada")
admin.site.register(Tour, TourAdmin)

class OpinionAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("user", "tour", "texto")
admin.site.register(Opinion, OpinionAdmin)

class SalidaAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "fechaInicio", "fechaFin", "asientos", "precio",
        "tour")
admin.site.register(Salida, SalidaAdmin)

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from tours.models import Tour, Zona

# Create your views here.
@login_required()
def index(request):
    """ Vista para entender la petición de la url / """

    # Se obtiene la lista de todos los Tours y Zonas
    tours = Tour.objects.all()
    zonas = Zona.objects.all()

    # Se determina si el usuario pertenece o no al grupo editores
    es_editor = request.user.groups.filter(name="editores").exists()

    return render(request, "tours/index.html",
        {"tours":tours, "zonas":zonas, "es_editor":es_editor})

@login_required()
def eliminar_tour(request, idTour):
    """
    Atiende la petición GET
       /tour/eliminar/<int:idTour>/
    """
    # Se obtienen los objetos correspondientes a los id's
    tour = Tour.objects.get(pk=idTour)

    # Se elimina el tour
    tour.delete()

    return redirect("/")

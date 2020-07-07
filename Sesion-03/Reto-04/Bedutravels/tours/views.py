from django.http import HttpResponse
from django.shortcuts import render

from tours.models import Tour, Zona

# Create your views here.
def index(request):
    """ Vista para entender la petición de la url / """

    # Se obtiene la lista de todos los Tours y Zonas
    tours = Tour.objects.all()
    zonas = Zona.objects.all()

    return render(request, "tours/index.html", {"tours":tours, "zonas":zonas})

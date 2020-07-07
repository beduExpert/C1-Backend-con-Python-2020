from django.http import HttpResponse
from django.shortcuts import render

from tours.models import Tour

# Create your views here.
def index(request):
    """ Vista para entender la petición de la url / """

    # Se obtiene la lista de todos los Tours
    tours = Tour.objects.all()

    return render(request, "tours/index.html", {"tours":tours})

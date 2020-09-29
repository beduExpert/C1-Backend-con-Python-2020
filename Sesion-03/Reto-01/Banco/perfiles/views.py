from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    """ Vista para atender la petición de la url /perfiles """

    return render(request, "perfiles/perfil.html")

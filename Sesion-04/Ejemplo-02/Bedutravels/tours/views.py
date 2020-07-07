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

    return render(request, "tours/index.html", {"tours":tours, "zonas":zonas})

def logout_user(request):
    """ Atiende las peticiones de GET /logout/ """

    logout(request)

    return redirect("/login/")

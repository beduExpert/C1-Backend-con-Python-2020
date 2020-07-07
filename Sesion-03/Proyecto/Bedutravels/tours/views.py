from django.http import HttpResponse
from django.shortcuts import render, redirect

from tours.models import Tour, Zona

# Create your views here.
def index(request):
    """ Vista para entender la petición de la url / """

    # Se obtiene la lista de todos los Tours y Zonas
    tours = Tour.objects.all()
    zonas = Zona.objects.all()

    return render(request, "tours/index.html", {"tours":tours, "zonas":zonas})

def login(request):
    """ Atiende las peticiones de GET /login/ """

    # Se definen los datos de un usuario válido
    usuario_valido = ("bedutravels", "bedutravels")  # (username, password)

    # Si hay datos vía POST se procesan
    if request.method == "POST":
        # Se obtienen los datos del formulario
        usuario_form = (request.POST["username"],
            request.POST["password"])
        if usuario_form == usuario_valido:
            # Tenemos usuario válido, redireccionamos a index
            return redirect("/")
        else:
            # Usuario malo
            msg = "Datos incorrectos, intente de nuevo!"
    else:
        # Si no hay datos POST
        msg = ""

    return render(request, "registration/login.html",
        {
            "msg":msg,
        }
    )

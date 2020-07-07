from django.contrib.auth import authenticate, login
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

def login_user(request):
    """ Atiende las peticiones de GET /login/ """

    # Se definen los datos de un usuario válido
    usuario_valido = ("bedutravels", "bedutravels")  # (username, password)

    # Si hay datos vía POST se procesan
    if request.method == "POST":
        # Se obtienen los datos del formulario
        next = request.GET.get("next", "/")
        acceso = authenticate(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if acceso is not None:
            # Tenemos usuario válido y agregamos datos
            # al request para mantener activa la sesión.
            login(request, acceso)

            # Redireccionamos a next
            return redirect(next)
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

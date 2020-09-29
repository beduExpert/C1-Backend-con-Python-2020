from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    """ Vista para entender la petición de la url / """

    return render(request, "tours/index.html")

from django.shortcuts import render
from rest_framework import viewsets

from .models import User, Zona, Tour, Salida
from .serializers import UserSerializer, ZonaSerializer, TourSerializer, SalidaSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API que permite realizar operaciones con la tabla User
    """
    # Se define el conjunto de datos sobre el que va a operar la vita,
    # en este caso, sobre todos los usuarios disponibles.
    queryset = User.objects.all().order_by('id')

    # Se define el serializador encargado de transformar las peticiones
    # de json a objetos django y viceversa.
    serializer_class = UserSerializer


class ZonaViewSet(viewsets.ModelViewSet):
    """
    API que permite realizar operaciones con la tabla Zona
    """
    # Se define el conjunto de datos sobre el que va a operar la vista,
    # en este caso, sobre todos las zonas disponibles.
    queryset = Zona.objects.all().order_by('id')

    # Se define el serializador encargado de transformar las peticiones
    # de json a objetos django y viceversa.
    serializer_class = ZonaSerializer


class TourViewSet(viewsets.ModelViewSet):
    """
    API que permite realizar operaciones con la tabla Tour
    """
    # Se define el conjunto de datos sobre el que va a operar la vista,
    # en este caso, sobre todos los tours disponibles.
    queryset = Tour.objects.all().order_by('id')

    # Se define el serializador encargado de transformar las peticiones
    # de json a objetos django y viceversa.
    serializer_class = TourSerializer


class SalidaViewSet(viewsets.ModelViewSet):
    """
    API que permite realizar operaciones con la tabla Salida
    """
    # Se define el conjunto de datos sobre el que va a operar la vista,
    # en este caso, sobre todos las salidas disponibles.
    queryset = Salida.objects.all().order_by('id')

    # Se define el serializador encargado de transformar las peticiones
    # de json a objetos django y viceversa.
    serializer_class = SalidaSerializer

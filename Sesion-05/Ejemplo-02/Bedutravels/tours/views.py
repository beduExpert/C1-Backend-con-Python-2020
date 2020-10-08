from django.shortcuts import render
from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer

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

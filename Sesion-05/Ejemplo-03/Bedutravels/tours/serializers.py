from rest_framework import serializers

from .models import User, Zona, Tour


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para User """
    class Meta:
        # Se define sobre que modelo actúa
        model = User
        # Se definen los campos a incluir
        fields = ('id', 'nombre', 'apellidos', 'email',
            'fechaNacimiento', 'genero', 'clave', 'tipo')


class TourSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Tour """
    class Meta:
        # Se define sobre que modelo actúa
        model = Tour
        # Se definen los campos a incluir
        fields = ('id', 'slug', 'nombre', 'operador', 'tipoDeTour',
            'descripcion', 'img', 'pais', 'zonaSalida', 'zonaLlegada')


class ZonaSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Zona """

    class Meta:
        # Se define sobre que modelo actúa
        model = Zona
        # Se definen los campos a incluir
        fields = ('id', 'nombre', 'descripcion', 'latitud', 'longitud',
            'tours_salida', 'tours_llegada')

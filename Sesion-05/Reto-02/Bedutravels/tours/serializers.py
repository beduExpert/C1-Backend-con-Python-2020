from rest_framework import serializers

from .models import User, Zona


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para User """
    class Meta:
        # Se define sobre que modelo actúa
        model = User
        # Se definen los campos a incluir
        fields = ('id', 'nombre', 'apellidos', 'email',
            'fechaNacimiento', 'genero', 'clave', 'tipo')


class ZonaSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Zona """
    class Meta:
        # Se define sobre que modelo actúa
        model = Zona
        # Se definen los campos a incluir
        fields = ('id', 'nombre', 'descripcion', 'latitud', 'longitud')

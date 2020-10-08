from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para User """
    class Meta:
        # Se define sobre que modelo actúa
        model = User
        # Se definen los campos a incluir
        fields = ('id', 'nombre', 'apellidos', 'email',
            'fechaNacimiento', 'genero', 'clave', 'tipo')
            

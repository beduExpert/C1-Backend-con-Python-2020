import graphene

from graphene_django.types import DjangoObjectType
from .models import User, Zona, Tour, Opinion, Salida


class UserType(DjangoObjectType):
    """ Tipo de dato para manejar el tipo User """
    class Meta:
        # Se relaciona con el origen de la data en models.User
        model = User

class ZonaType(DjangoObjectType):
    """ Tipo de dato para manejar el tipo Zona """
    class Meta:
        # Se relaciona con el origen de la data en models.Zona
        model = Zona

class TourType(DjangoObjectType):
    """ Tipo de dato para manejar el tipo Tour """
    class Meta:
        # Se relaciona con el origen de la data en models.Tour
        model = Tour

class SalidaType(DjangoObjectType):
    """ Tipo de dato para manejar el tipo Salida """
    class Meta:
        # Se relaciona con el origen de la data en models.Salida
        model = Salida


class Query(graphene.ObjectType):
    """ Definición de las respuestas a las consultas posibles """

    # Se definen los posibles campos en las consultas
    all_users = graphene.List(UserType)  # allUsers
    all_zonas = graphene.List(ZonaType)  # allZonas
    all_tours = graphene.List(TourType)  # allTours
    all_salidas = graphene.List(SalidaType)  # allSalidas

    # Se define las respuestas para cada campo definido
    def resolve_all_users(self, info, **kwargs):
        # Responde con la lista de todos registros
        return User.objects.all()

    def resolve_all_zonas(self, info, **kwargs):
        # Responde con la lista de todos registros
        return Zona.objects.all()

    def resolve_all_tours(self, info, **kwargs):
        # Responde con la lista de todos registros
        return Tour.objects.all()

    def resolve_all_salidas(self, info, **kwargs):
        # Responde con la lista de todos registros
        return Salida.objects.all()


class CrearZona(graphene.Mutation):
    """ Permite realizar la operación de crear en la tabla Zona """

    class Arguments:
        """ Define los argumentos para crear una Zona """
        nombre = graphene.String(required=True)
        descripcion = graphene.String()
        latitud = graphene.Decimal()
        longitud = graphene.Decimal()

    # El atributo usado para la respuesta de la mutación
    zona = graphene.Field(ZonaType)

    def mutate(self, info, nombre, descripcion=None, latitud=None,
        longitud=None):
        """
        Se encarga de crear la nueva Zona donde sólo nombre es obligatorio, el
        resto de los atributos son opcionales.
        """
        zona = Zona(
            nombre=nombre,
            descripcion=descripcion,
            latitud=latitud,
            longitud=longitud
        )
        zona.save()

        # Se regresa una instancia de esta mutación y como parámetro la Zona
        # creada.
        return CrearZona(zona=zona)


class EliminarZona(graphene.Mutation):
    """ Permite realizar la operación de eliminar en la tabla Zona """
    class Arguments:
        """ Define los argumentos para eliminar una Zona """
        id = graphene.ID(required=True)

    # El atributo usado para la respuesta de la mutación, en este caso sólo se
    # indicará con la variuable ok true en caso de éxito o false en caso
    # contrario
    ok = graphene.Boolean()

    def mutate(self, info, id):
        """
        Se encarga de eliminar la nueva Zona donde sólo es necesario el atributo
        id y además obligatorio.
        """
        try:
            # Si la zona existe se elimina sin más
            zona = Zona.objects.get(pk=id)
            zona.delete()
            ok = True
        except Zona.DoesNotExist:
            # Si la zona no existe, se procesa la excepción
            ok = False
        # Se regresa una instancia de esta mutación
        return EliminarZona(ok=ok)


class Mutaciones(graphene.ObjectType):
    crear_zona = CrearZona.Field()
    eliminar_zona = EliminarZona.Field()


# Se crea un esquema que hace uso de la clase Query
schema = graphene.Schema(query=Query, mutation=Mutaciones)

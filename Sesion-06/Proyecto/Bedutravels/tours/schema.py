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


class ModificarZona(graphene.Mutation):
    """ Permite realizar la operación de modificar en la tabla Zona """
    class Arguments:
        """ Define los argumentos para modificar una Zona """
        id = graphene.ID(required=True)
        nombre = graphene.String()
        descripcion = graphene.String()
        longitud = graphene.Float()
        latitud = graphene.Float()

    # El campo regresado como respuesta de la mutación, en este caso se regresa
    # la zona modificada.
    zona = graphene.Field(ZonaType)

    def mutate(self, info, id, nombre=None, descripcion=None, longitud=None,
        latitud=None):
        """
        Se encarga de modificar la Zona identificada por el id.
        """
        try:
            # Si la zona existe se modifica
            zona = Zona.objects.get(pk=id)
            # Si algunos de los atributos es proporcionado, entonces se
            # actualiza
            if nombre is not None:
              zona.nombre = nombre
            if descripcion is not None:
              zona.descripcion = descripcion
            if latitud is not None:
              zona.latitud = latitud
            if longitud is not None:
              zona.longitud = longitud
            zona.save()
        except Zona.DoesNotExist:
            # Si la zona no existe, se procesa la excepción
            zona = None
        # Se regresa una instancia de esta mutación
        return ModificarZona(zona=zona)


class CrearTour(graphene.Mutation):
    """ Permite realizar la operación de crear en la tabla Tour """

    class Arguments:
        """ Define los argumentos para crear un Tour """
        nombre = graphene.String(required=True)
        descripcion = graphene.String(required=True)
        idZonaSalida = graphene.ID(required=True)
        idZonaLlegada = graphene.ID(required=True)
        slug = graphene.String()
        operador = graphene.String()
        tipoDeTour = graphene.String()
        img = graphene.String()
        pais = graphene.String(required=False)

    # El atributo usado para la respuesta de la mutación
    tour = graphene.Field(TourType)

    def mutate(self, info, nombre, descripcion, idZonaSalida, idZonaLlegada,
        slug=None, operador=None, tipoDeTour=None, img=None, pais=None):
        """
        Se encarga de crear un nuevo Tour

        Los atributos obligatorios son:
        - nombre
        - descripcion
        - idZonaSalida
        - idZonaLlegada

        Los atributos opcionales son:
        - slug
        - operador
        - tipoDeTour
        - img
        - pais
        """
        zonaSalida = Zona.objects.get(pk=idZonaSalida)
        zonaLlegada = Zona.objects.get(pk=idZonaLlegada)
        tour = Tour(
            nombre=nombre,
            descripcion=descripcion,
            zonaSalida=zonaSalida,
            zonaLlegada=zonaLlegada,
            slug=slug,
            operador=operador,
            tipoDeTour=tipoDeTour,
            img=img,
            pais=pais
        )
        tour.save()

        # Se regresa una instancia de esta mutación
        return CrearTour(tour=tour)


class ModificarTour(graphene.Mutation):
    """ Permite realizar la operación de modificar en la tabla Tour """

    class Arguments:
        """ Define los argumentos para modificar un Tour """
        id = graphene.ID(required=True)
        nombre = graphene.String()
        descripcion = graphene.String()
        idZonaSalida = graphene.ID()
        idZonaLlegada = graphene.ID()
        slug = graphene.String()
        operador = graphene.String()
        tipoDeTour = graphene.String()
        img = graphene.String()
        pais = graphene.String()

    # El atributo usado para la respuesta de la mutación
    tour = graphene.Field(TourType)

    def mutate(self, info, id, nombre=None, descripcion=None, idZonaSalida=None,
        idZonaLlegada=None, slug=None, operador=None, tipoDeTour=None,
        img=None, pais=None):
        """
        Se encarga de modificar un nuevo Tour

        Los atributos obligatorios son:
        - id

        Los atributos opcionales son:
        - nombre
        - descripcion
        - idZonaSalida
        - idZonaLlegada
        - slug
        - operador
        - tipoDeTour
        - img
        - pais
        """
        tour = Tour.objects.get(pk=id)
        if nombre is not None:
            tour.nombre = nombre
        if slug is not None:
            tour.slug = slug
        if idZonaSalida is not None:
            zonaSalida = Zona.objects.get(pk=idZonaSalida)
            tour.zonaSalida = zonaSalida
        if idZonaLlegada is not None:
            zonaLlegada = Zona.objects.get(pk=idZonaLlegada)
            tour.zonaLlegada = zonaLlegada
        if descripcion is not None:
            tour.descripcion = descripcion
        if operador is not None:
            tour.operador = operador
        if tipoDeTour is not None:
            tour.tipoDeTour = tipoDeTour
        if img is not None:
            tour.img = img
        if pais is not None:
            tour.pais = pais
        tour.save()

        # Se regresa una instancia de esta mutación
        return ModificarTour(tour=tour)


class EliminarTour(graphene.Mutation):
    """ Permite realizar la operación de eliminar en la tabla Tour """

    class Arguments:
        """ Define los argumentos para eliminar un Tour """
        id = graphene.ID(required=True)

    # El atributo usado para la respuesta de la mutación
    ok = graphene.Boolean()

    def mutate(self, info, id):
        """
        Se encarga de eliminar un Tour

        Los atributos obligatorios son:
        - id
        """
        try:
            # Si el Tour existe, se elimina
            tour = Tour.objects.get(pk=id)
            tour.delete()
            ok = True
        except Tour.DoesNotExist:
            ok = False

        # Se regresa el estado de la operación
        return EliminarTour(ok=ok)


class Mutaciones(graphene.ObjectType):
    crear_zona = CrearZona.Field()
    eliminar_zona = EliminarZona.Field()
    modificar_zona = ModificarZona.Field()
    crear_tour = CrearTour.Field()
    modificar_tour = ModificarTour.Field()
    eliminar_tour = EliminarTour.Field()


# Se crea un esquema que hace uso de la clase Query
schema = graphene.Schema(query=Query, mutation=Mutaciones)

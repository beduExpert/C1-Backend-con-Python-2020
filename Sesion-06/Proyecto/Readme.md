[`Backend con Python`](../../Readme.md) > [`Sesión 06`](../Readme.md) > Proyecto
## Creando una API GraphQL con todas las operaciones CRUD sobre una tabla

### OBJETIVOS
- Aplicar el concepto de mutaciones de GraphQL
- Crear una mutación para cada operación CRUD para la tabla Tour

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-06/Proyecto`
1. Activar el entorno virtual __Bedutravels__
1. Diagrama de entidad-relación del proyecto Bedutravels
   ![Diagrama entidad-relación](assets/bedutravels-modelo-er.png)

### DESARROLLO
1. La operación de lectura (read) o consultas ya se ha realizado con anterioridad, así que se puede continuar con la operación de agregar (create).

1. Se crea la operación agregar nuevo registros a la __API GraphQL__ para la tabla __Tour__

   __Se crea la mutación en el archivo `Bedutravels/tours/schema.py`:__

   ```python
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
           pais = graphene.String()

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
   ```
   No olvidar colocar la opción `required=True` para los argumentos obligatorios, así como en el método `mutate()` indicar los argumentos opciones con valor `None`.

   Considerar que la tabla __Tour__ está relacionada con la tabla __Zona__, así que para crear un nuevo tour, es necesario primero obtener las zonas relacionadas.

   __Se agrega a la clase de la lista de mutaciones:__

   ```python
   class Mutaciones(graphene.ObjectType):
       crear_zona = CrearZona.Field()
       eliminar_zona = EliminarZona.Field()
       modificar_zona = ModificarZona.Field()
       crear_tour = CrearTour.Field()
   ```

1. Se agrega un nuevo __Tour__ usando los siguientes datos:

   - Nombre: Purepecha
   - Slug: mexico
   - Operador: Mochilazo
   - Tipo de tour: Tour en grupo
   - Descripción: Descubre las historias milenarias de los Purepecha
   - img: https://i.imgur.com/vVq652d.jpg
   - pais: México
   - Zona de salida: Ciudad de México
   - Zona de llegada: Michoacán

   __La mutación en GraphQL es:__

   ```json
   mutation CrearTour {
     crearTour(
       nombre:"Purepecha",
       slug:"mexico",
       operador:"Mochilazo",
       tipoDeTour:"Tour en grupo",
       descripcion:"Descubre las historias milenarias de los Purepechas",
       img:"https://i.imgur.com/vVq652d.jpg",
       pais:"México",
       idZonaSalida:"1",
       idZonaLlegada:"12"
     ) {
       tour {
         id
         nombre
         descripcion
         zonaSalida {
           id
           nombre
         }
         zonaLlegada {
           id
           nombre
         }
       }
     }
   }
   ```
   __Obteniendo un resultado similar a:__

   ```json
   {
     "data": {
       "crearTour": {
         "tour": {
           "id": "4",
           "nombre": "Purepecha",
           "descripcion": "Descubre las historias milenarias de los Purepechas",
           "zonaSalida": {
             "id": "1",
             "nombre": "Ciudad de México"
           },
           "zonaLlegada": {
             "id": "12",
             "nombre": "Michoacán"
           }
         }
       }
     }
   }   
   ```
   ***

1. Se crea la operación modificar para la tabla __Tour__

   __Se crea la mutación en el archivo `Bedutravels/tours/schema.py`:__

   ```python
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
           )
           tour.save()

           # Se regresa una instancia de esta mutación
           return ModificarTour(tour=tour)
   ```
   Considera que para modificar un __Tour__ necesitamos saber cual y para ello se requiere del __id__.

   En el caso de modificar las zonas, considerar que es una relación a la tabla Zona, por lo que hay que buscar la zona con el nuevo id.

   __Se agrega a la clase de la lista de mutaciones:__

   ```python
   class Mutaciones(graphene.ObjectType):
       crear_zona = CrearZona.Field()
       eliminar_zona = EliminarZona.Field()
       modificar_zona = ModificarZona.Field()
       crear_tour = CrearTour.Field()
       modificar_tour = ModificarTour.Field()
   ```

1. Se agrega un nuevo __Tour__ usando los siguientes datos:

   - Nombre: Yacatas
   - Slug: mexico
   - Operador: Mochilazo
   - Tipo de tour: Tour en grupo
   - Descripción: Templos religiosos del Imperio Tarascan, rivales a los Aztecas
   - pais: México
   - Zona de salida: Ciudad de México
   - Zona de llegada: Michoacán

   __La mutación en GraphQL es:__

   ```json
   mutation CrearTour {
     crearTour(
       nombre:"Yacatas",
       slug:"mexico",
       operador:"Mochilazo",
       tipoDeTour:"Tour en grupo",
       descripcion:"Templos religiosos del Imperio Tarascan, rivales a los Aztecas",
       pais:"México",
       idZonaSalida:"1",
       idZonaLlegada:"12"
     ) {
       tour {
         id
         nombre
         descripcion
         zonaSalida {
           id
           nombre
         }
         zonaLlegada {
           id
           nombre
         }
       }
     }
   }
   ```

   __Modificando el tour anterior agregando la url de la imagen:__

   - Imágen: https://i.imgur.com/jJuy1vU.jpg

   ```json
   mutation ModificarTour {
     modificarTour(
       id:"5",
       img:"https://i.imgur.com/jJuy1vU.jpg"
     ) {
       tour {
         id
         nombre
         img
       }
     }
   }
   ```

   __Obteniendo un resultado similar a:__

   ```json
   {
     "data": {
       "modificarTour": {
         "tour": {
           "id": "5",
           "nombre": "Yacatas",
           "img": "https://i.imgur.com/jJuy1vU.jpg"
         }
       }
     }
   }
   ```
   ***

1. Se crea la operación eliminar para la tabla __Tour__

   __Se crea la mutación en el archivo `Bedutravels/tours/schema.py`:__

   ```python
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
   ```
   Considera que para eliminar un __Tour__ necesitamos saber cual y para ello se requiere del __id__.

   Como el tour será eliminado, no se puede regresar como valor, por esa razón se usa la variable __ok__ para indicar el estado de la operación.

   __Se agrega a la clase de la lista de mutaciones:__

   ```python
   class Mutaciones(graphene.ObjectType):
       crear_zona = CrearZona.Field()
       eliminar_zona = EliminarZona.Field()
       modificar_zona = ModificarZona.Field()
       crear_tour = CrearTour.Field()
       modificar_tour = ModificarTour.Field()
       eliminar_tour = EliminarTour.Field()
   ```

1. Se agrega un nuevo __Tour__ usando los siguientes datos:

   - Nombre: Luciérnas salvajes
   - Descripción: Viven en carne propia ser perseguido y devorado por miles de Luciérnagas.
   - Zona de salida: Ciudad de México
   - Zona de llegada: Yucatán

   __La mutación en GraphQL es:__

   ```json
   mutation CrearTour {
     crearTour(
       nombre:"Luciérnagas salvajes",
       descripcion: "Viven en carne propia ser perseguido y devorado por miles de Luciérnagas."
       idZonaSalida:"1",
       idZonaLlegada:"4"
     ) {
       tour {
         id
         nombre
         descripcion
         zonaSalida {
           id
           nombre
         }
         zonaLlegada {
           id
           nombre
         }
       }
     }
   }
   ```

   __Eliminando el tour anterior:__

   ```json
   mutation EliminarTour {
     eliminarTour(id:"6") {
       ok
     }
   }
   ```

   __Obteniendo un resultado similar a:__

   ```json
   {
     "data": {
       "eliminarTour": {
         "ok": true
       }
     }
   }
   ```
   ***

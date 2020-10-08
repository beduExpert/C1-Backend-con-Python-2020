`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 05`](../Readme.md) > Proyecto
## Creando un API para realizar las operaciones CRUD de una tabla

### OBJETIVOS
- Agregar la relación entre los modelos __Tour__ y __Salida__.
- Realizar operaciones de CRUD vía API para la tabla __Salida__ incluyendo los tours asociados.

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-05/Proyecto`
1. Activar el entorno virtual __Bedutravels__
1. Diagrama de entidad-relación del proyecto Bedutravels

   ![Diagrama entidad-relación](assets/bedutravels-modelo-er.png)

### DESARROLLO
1. Se modifica el archivo `serializers.py` para que se muestre la lista de salidas:

   ```python
   class SalidaSerializer(serializers.HyperlinkedModelSerializer):
       """ Serializador para atender las conversiones para Salida """
       class Meta:
           # Se define sobre que modelo actúa
           model = Salida
           # Se definen los campos a incluir
           fields = ('id', 'fechaInicio', 'fechaFin', 'asientos', 'precio', 'tour')
   ```

   __Se agrega la url `/api/salidas/`:__

   ```python
   router.register(r'salidas', views.SalidaViewSet)   
   ```

   __Se agrega la vista:__

   ```python
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
   ```

   __El resultado debe ser como el siguiente:__

   ![Lista de salidas](assets/api-salidas-01.png)
   ***

1. Se actualiza el serializador `TourSerializer` en el archivo `Bedutravels/tours/serializers.py` para agregar el campo `salidas` para que muestre la lista de salidas por cada tour:

   ```python        
           # Se definen los campos a incluir
           fields = ('id', 'slug', 'nombre', 'operador', 'tipoDeTour',
               'descripcion', 'img', 'pais', 'zonaSalida', 'zonaLlegada',
               'salidas')
   ```
   ***

1. Acceso y uso de la __API__ `/api/tours`

   __Para tener acceso al API abrir la siguiente url:__

   http://localhost:8000/api/tours/

   Se deberá de observar algo similar a lo siguiente:

   ![bedutravels API tours con salidas](assets/api-salidas-02.png)

   __Para tener acceso al detalle del tour con id=1 abrir la siguiente url:__

   http://localhost:8000/api/tour/1/

   Se deberá de observar algo similar a lo siguiente:

   ![bedutravels API un tour](assets/api-salidas-03.png)
   ***

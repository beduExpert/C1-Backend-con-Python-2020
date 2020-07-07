[`Backend con Python`](../../Readme.md) > [`Sesión 04`](../Readme.md) > Ejemplo-03
## Definiendo las consultas usando el ORM de Django

### OBJETIVO
- Conocer y comprender el sistema de consultas o Object Relacional Mapping (ORM) de Django.
- Conocer las consultas entre tablas y sus relaciones
- Definir una consulta para generar un reporte.

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-04/Ejemplo-03`
1. Diagrama del modelo entidad-relación para el proyect __Bedutravels__

   ![Modelo entidad-relación para Bedutravels](assets/bedutravels-modelo-er.jpg)

1. Documentación de Django referente a modelos:
   - Referencia a la API de Modelos en Django https://docs.djangoproject.com/en/2.2/ref/models/

### DESARROLLO
1. Usando el __Shell de Django__ mostrar todos los registros de la tabla Zona:

   __Iniciando el Shell de Django:__
   ```console
   (Bedutravels) Ejemplo-03/Bedutravels $ python manage.py shell
   Python 3.7.3 (default, Mar 27 2019, 22:11:17)
   [GCC 7.3.0] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   (InteractiveConsole)
   >>>
   ```

   __Realizando la consulta para obtener todos los registros de la tabla Zona:__

   ```python
   >>> from tours.models import Zona
   >>> Zona.objects.all()
   <QuerySet [<Zona: Ciudad de México>, <Zona: Yucatán>, <Zona: Chiapas>, <Zona: Guanajuato>]>
   >>>
   ```
   ***

1. Imprime los datos de la zona con `id = 3`:

   __Dentro el Shell de Django:__

   ```python
   >>> z3 = Zona.objects.get(pk=3)
   >>> z3
   <Zona: Chiapas>
   >>> print(z3.id, z3.nombre, z3.descripcion, z3.latitud, z3.longitud)
   3 Chiapas Chiapas None None
   >>>
   ```
   ***

1. Imprime los tours de la zona __Ciudad de México__ haciendo uso de la relacion entre Tour y Zona:

   __Dentro el Shell de Django:__

   ```python
   >>> from tours.models import Tour
   >>> Tour.objects.filter(zona__nombre="Ciudad de México")
   <QuerySet [<Tour: Chiapas Hermoso>, <Tour: Guanajuato por siempre>, <Tour: Yucatán y naturaleza>]>
   ```
   ***

1. Imprime la lista de todos los tours cuya zona de salida sea  __Ciudad de México__ incluyendo nombre de zona, id de tour y nombre de tour.

   __Dentro el Shell de Django:__

   ```python
   >>> from tours.models import Zona, Tour
   >>> z1 = Zona.objects.get(pk=1)  # Zona de Ciudad de México
   >>> z1
   <Zona: Ciudad de México>
   >>> for tour in z1.tours_salida.all():
   ...     print(z1, tour.id, tour)
   ...
   Ciudad de México 1 Chiapas Hermoso
   Ciudad de México 2 Guanajuato por siempre
   Ciudad de México 3 Yucatán y naturaleza
   >>>
   ```
   ***

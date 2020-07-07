[`Backend con Python`](../../Readme.md) > [`Sesión 04`](../Readme.md) > Reto-03
## Definiendo las consultas usando el ORM de Django

### OBJETIVO
- Crear consultas entre tablas y sus relaciones
- Definir una consulta para generar un reporte.

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-04/Reto-03`
1. Diagrama del modelo entidad-relación para el proyecto __Bedutravels__

   ![Modelo entidad-relación para Bedutravels](assets/bedutravels-modelo-er.jpg)

1. Documentación de Django referente a modelos:
   - Referencia a la API de Modelos en Django https://docs.djangoproject.com/en/2.2/ref/models/

### DESARROLLO
1. Imprime la lista de todas las Zonas, en cada Zona incluir id, nombre, lista de tours que salen de esa zona, en cada Tour incluir id, nombre, lista de salidas para ese tour y para cada Salida incluir id, fechaInicio, fechaFin.

   __Dentro el Shell de Django:__

   ```python
   >>> from tours.models import Zona, Tour, Salida
   >>> zonas = Zona.objects.all()
   >>> zonas
   <QuerySet [<Zona: Ciudad de México>, <Zona: Yucatán>, <Zona: Chiapas>, <Zona: Guanajuato>]>
   >>> for zona in zonas:
   ...     print(zona.id, zona)
   ...     for tour in zona.tours_salida.all():
   ...         print("   ", tour.id, tour)
   ...         for salida in tour.salidas.all():
   ...             print("   "*2, salida.id, salida.fechaInicio, salida.fechaFin)
   ...

   1 Ciudad de México
       1 Chiapas Hermoso
          1 2019-06-21 2019-06-26
          2 2019-07-03 2019-07-08
          3 2019-07-09 2019-07-14
       2 Guanajuato por siempre
          4 2019-07-21 2019-07-26
          5 2019-08-03 2019-08-03
          6 2019-08-03 2019-08-03
          7 2019-08-09 2019-08-14
       3 Yucatán y naturaleza
          8 2019-08-22 2019-08-26
          9 2019-08-22 2019-08-27
          10 2019-09-13 2019-09-19
   2 Yucatán
   3 Chiapas
   4 Guanajuato
   >>>
   ```
   ***

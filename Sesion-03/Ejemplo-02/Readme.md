[`Backend con Python`](../../Readme.md) > [`Sesión 03`](../Readme.md) > Ejemplo-02
## Creando relaciones con el modelo de datos de Django

### OBJETIVO
- Crear una relación entre dos tablas

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-03/Ejemplo-02`
1. Diagrama del modelo entidad-relación para el proyecto __Bedutravels__

   ![Modelo entidad-relación para Bedutravels](assets/bedutravels-modelo-er.jpg)

1. Documentación de Django referente a modelos:
   - Descripción de modelos y ejemplos: https://docs.djangoproject.com/en/2.2/topics/db/models/
   - Referencia a la API de Modelos en Django https://docs.djangoproject.com/en/2.2/ref/models/
   - Referencia a los tipos de datos que maneja Django https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types

### DESARROLLO
1. Usando el modelo entidad-relación, crear la tabla Tour y su relación con la tabla Zona.

   ```python
   class Tour(models.Model):
       """ Define la tabla Tour """
       nombre = models.CharField(max_length=145)
       slug = models.CharField(max_length=45, null=True, blank=True)
       operador = models.CharField(max_length=45, null=True, blank=True)
       tipoDeTour = models.CharField(max_length=45, null=True, blank=True)
       descripcion = models.CharField(max_length=256)
       img = models.CharField(max_length=256, null=True, blank=True)
       pais = models.CharField(max_length=45, null=True, blank=True)
       zonaSalida = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True,
           blank=True, related_name="tours_salida")
       zonaLlegada = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True,
           blank=True, related_name="tours_llegada")

       def __str__(self):
           return "{}".format(self.nombre)
   ```
   Observar el uso del tipo de dato de Django ForeignKey donde el parámetro `on_delete=models.SET_NULL` indica que en caso de que la Zona se borre, el registro relacionado en Tour se asigne un valor de nulo.

   Además, el sistema de consultas (query) de Django permite, desde una Zona encontrar todos los Tours relacionados con una Zona mediante `Zona.tours_salida.all()` o 'Zona.tours_llegada.all()', según sea el caso, esto es gracias al parámetro `related_name`.

   __Avisando a Django que hemos modificado el archivo `models.py`:__

   ```console
   (Bedutravels) Ejemplo-02/Bedutravels $ python manage.py makemigrations
   (Bedutravels) Ejemplo-02/Bedutravels $ python manage.py migrate
   (Bedutravels) Ejemplo-02/Bedutravels $
   ```

   __Agregando la tabla Tour al administrador de Django y definiendo los campos a mostrar:__

   ```python
   from .models import Zona, User, Tour

   class TourAdmin(admin.ModelAdmin):
       # Se sobre escribe lo que hace __str__
       list_display = ("id", "nombre", "slug", "operador", "tipoDeTour",
           "descripcion", "pais", "zonaSalida", "zonaLlegada")
   admin.site.register(Tour, TourAdmin)
   ```
   Abrimos el navegador en la siguiente url ...

   Abrir la url http://localhost:8000/admin y usar los siguientes datos para entrar:
   - Zona: bedutravels
   - Clave: bedutravels

   Al agregar un __Tour__ en el panel de administración de Django se puede observar como las relaciones con la tabla __Zona__ se muestran como listas de selección como se muestra a continuación:

   ![Django Admin](assets/admin-01.png)   

   Después de agregar el tour ...

   ![Django Admin](assets/admin-02.png)
   ***

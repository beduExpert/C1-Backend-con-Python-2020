[`Backend con Python`](../../Readme.md) > [`Sesión 04`](../Readme.md) > Reto-02
## Creando relaciones con el modelo de datos de Django

### OBJETIVO
- Crear una relación entre dos tablas.

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-04/Reto-02`
1. Diagrama del modelo entidad-relación para el proyecto __Bedutravels__

   ![Modelo entidad-relación para Bedutravels](assets/bedutravels-modelo-er.png)

1. Documentación de Django referente a modelos:
   - Descripción de modelos y ejemplos: https://docs.djangoproject.com/en/2.2/topics/db/models/
   - Referencia a la API de Modelos en Django https://docs.djangoproject.com/en/2.2/ref/models/
   - Referencia a los tipos de datos que maneja Django https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types

### DESARROLLO
1. Usando el modelo entidad-relación, agregar la tabla Salida:

   ```python
   class Salida(models.Model):
       """ Define la tabla Salida """
       fechaInicio = models.DateField()
       fechaFin = models.DateField()
       asientos = models.PositiveSmallIntegerField(null=True, blank=True)
       precio = models.DecimalField(max_digits=10, decimal_places=2)
       tour = models.ForeignKey(Tour, related_name="salidas", on_delete=models.CASCADE)

       def __str__(self):
           return "{} ({}, {})".format(self.tour, self.fechaInicio, self.fechaFin)
   ```

   __Avisando a Django que hemos modificado el archivo `models.py`:__

   ```console
   (Bedutravels) Reto-02/Bedutravels $ python manage.py makemigrations
   (Bedutravels) Reto-02/Bedutravels $ python manage.py migrate
   (Bedutravels) Reto-02/Bedutravels $
   ```

   __Agregando el modelo Salida a el archivo `admin.py`:__

   ```python
   class SalidaAdmin(admin.ModelAdmin):
       # Se sobre escribe lo que hace __str__
       list_display = ("id", "fechaInicio", "fechaFin", "asientos", "precio",
           "tour")

   admin.site.register(Salida, SalidaAdmin)
   ```

   Después de agregar 3 Salida para el Tour de Chiapas Hermoso se observa:

   ![Django admin agregando una Salida](assets/admin-01.png)
   ***

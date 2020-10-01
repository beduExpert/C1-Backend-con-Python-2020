`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 03`](../Readme.md) > Ejemplo-04
## El sistema de plantillas de Django

### OBJETIVO
- Hacer uso del sistema de consultas de Django.
- Conocer el sistemas de plantillas de Django
- Aplicar las consultas en las plantillas de Django.

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-03/Ejemplo-04`
1. Diagrama del modelo entidad-relación para el proyecto __Bedutravels__

   ![Modelo entidad-relación para Bedutravels](bedutravels-modelo-er.png)

1. Documentación de Django referente a modelos:
   - Referencia a la API de Modelos en Django https://docs.djangoproject.com/en/2.2/ref/models/
   - Expresiones en consultas: https://docs.djangoproject.com/en/2.2/ref/models/expressions/
   - API de consultas https://docs.djangoproject.com/en/2.2/ref/models/querysets/

### DESARROLLO
1. Modificar la vista `index()` para que haga uso de las consultas de Django para obtener cada uno de los registros necesarios para mostrar en la lista de Tours

   __Realizando cambios al archivo `Bedutravels/tours/views.py`:__
   ```python
   from .models import Zona, Tour

   # Create your views here.
   def index(request):
       """ Vista para atender la petición de la url / """
       # Obteniendo los datos mediantes consultas
       tours = Tour.objects.all()

       return render(request, "tours/index.html", {"tours":tours})
   ```
   ***

1. Modificar la plantilla `index.html` para que haga uso de los resultados obtenidos en la vista:

   __Realizando cambios al archivo `Bedutravels/tours/template/tours/index.html`:__
   ```html
   <section id="central">

      {% for tour in tours %}
      <div class="tour-container">
        <div class="card-image-container">
          <img src="{{ tour.img }}" alt="{{ tour }}">
        </div>
        <div class="card-content">
          <div>
            <h3>{{ tour.nombre }}</h3>
            <p class="margin-bottom-sm">
              {{ tour.descripcion }}
            </p>

            <table class="table-info-tour">
              <tbody>
                <tr>
                  <th>Salida / Llegada </th>
                  <td>{{ tour.zonaSalida }}/{{ tour.zonaLlegada }}</td>
                </tr>
                <tr>
                  <th>Operador</th>
                  <td>{{ tour.operador }}</td>
                </tr>
                <tr>
                  <th>Tipo de tour</th>
                  <td>{{ tour.tipoDeTour }}</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="">
            <button class="button-tour">Ver tour</button>
          </div>
        </div>
      </div>
      {% endfor %}

    </section>
   ```
   ***

__Resultado final:__

![Index dinámico](assets/index-01.png)

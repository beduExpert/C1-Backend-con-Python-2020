[`Backend con Python`](../../Readme.md) > [`Sesión 05`](../Readme.md) > Postwork
## Aplicar los conceptos de la clase a tú Proyecto

### OBJETIVOS
- Aplicar el concepto Django Rest a tú Proyecto
- Crear cada operación CRUD para las tablas de tú Proyecto en el API

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-05/Postwork`

### DESARROLLO
1. __INSTALACIÓN__ de Djanfo Rest Framework se realiza con el comando `pip install djangorestframework`

   __Se actualiza el archivo `requeriments.txt` para incluir el módulo instalado__

1. Agregando Djanfo Rest Framework a la configuración en el archivo `settings.py` como una aplicación adicional.

1. Crear la ruta en la url `/api/???` para cada tabla en tu modelo modificando el archivo `Proyecto/Proyecto/urls.py`.

1. Se crea la vista para cada tabla en el archivo `Proyecto/miapp/views.py` que hace uso de su serializador correspondiente.

1. Se crea el serializador para cada tabla en el archivo `Proyecto/miapp/serializers.py`.

1. Validar el acceso y uso de la __API__ `/api/???` en la url http://localhost:8000/api/???

   Realizar operaciones de agregar, listar, modificar y eliminar registros a cada una de las tablas.

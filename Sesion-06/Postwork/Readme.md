[`Backend con Python`](../../Readme.md) > [`Sesión 06`](../Readme.md) > Postwork
## Aplicar los conceptos de la clase a tú Proyecto

### OBJETIVOS
- Aplicar el concepto API GraphQL a tú Proyecto
- Crear cada operación CRUD para las tablas de tú Proyecto

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-06/Postwork`

### DESARROLLO
1. __INSTALACIÓN__ de Django Graphene se realiza con el comando `pip install graphene-django`

   __Se actualiza el archivo `requeriments.txt` para incluir el módulo instalado__

1. Agregando Django Graphene a la configuración en el archivo `settings.py` como una aplicación adicional.

1. Se crea la ruta para la url `/graphql` modificando el archivo `Bedutravels/tours/urls.py`.

1. Se crea el esquema (schema) en el archivo `Proyecto/miapp/schema.py` para atender las peticiones.

   Finalmente se crea la variable `schema` que define el esquema de los posibles campos y consultas.

1. Validar el acceso y uso de la __API__ `/graphql` en la url http://localhost:8000/graphql

1. Crear la operación agregar a la __API GraphQL__ para las tabla de tu Proyecto.

   Validar que la operación agregar, adicionando nuevos datos a cada tabla

1. Crear la operación modificar para para cada tabla.

  Validar que la operación modificar, realizando cambios en los datos de cada tabla

1. Crear la operación eliminar para las tablas de tu Proyecto.

  Validar que la operación eliminar, agregando nuevos datos y eliminandolos posteriormente.

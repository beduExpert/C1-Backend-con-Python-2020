`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 02`](../Readme.md) > Ejemplo-03

## Conociendo la interface WSGI creando una micro aplicación web con Python.

### OBJETIVO
Comprender el flujo de información entre un servidor web y una aplicación en Python por medio de la interface WSGI (Web Server Gateway Interface).

#### REQUISITOS
1. Actualizar repositorio

#### DESARROLLO
1. Entendiendo la interface WSGI: Creando la aplicación web en la carpeta `webapp/` con el nombre `info.py` que muestre la información de la variables de ambiente que recibe una aplicación web

   __Cambiarse a la carpeta `webapp`:__
   ```console
   Sesion-02/Ejemplo-03 $ cd webapp
   Sesion-02/Ejemplo-03/webapp $
   ```

   __Ejecutando el script con:__
   ```console
   Sesion-02/Ejemplo-03/webapp $ python info.py
   Esuchando en localhost:8000... [Presiona Control+C para terminar!]

   Abre la siguiente url en tu navegador:

   	http://localhost:8000
   ```
   El servidor se inicia en localhost del equipo en el puerto 8000 quedando en espera de peticiones hasta que se presione Control+C.

   Se puede acceder abriendo la siguiente url en algún navegador:
   - http://localhost:8000

1. ¿Qué sucede si se abre la siguiente petición?

   - http://localhost:8000/?nombre=rctorr

   Lo anterior es una petición GET que bien podría ser creada por un formulario donde se está solicitando el nombre al usuario...
   ***

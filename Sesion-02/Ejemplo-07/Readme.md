`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 02`](../Readme.md) > Ejemplo-04
## Automatizando la ejecución de archivos SQL con Python

### OBJETIVO
Conocer la forma de construir un script en Python para ejecutar instrucciones SQL por medio de archivos para el proyecto Biblioteca.

#### REQUISITOS
1. Carpeta de repo actualizada
1. Usar la carpeta de trabajo `Sesion-02/Ejemplo-07`

#### DESARROLLO
1. Crear el script `sql2mysql.py` que reciba como parámetro el nombre de un archivo con extensión sql y ejecute las instrucciones en un servidor MariaDB.

   __Ejecutando el script con el archivo `sql/tablas-inicial.sql`:__

    ```bash
    Sesion-02/Ejemplo-07 $ python sql2mysql.py sql/tablas-inicial.sql

    Se ha ejecutado el archivo sql/tablas-inicial.sql correctamente
    ```

    __Lista de los nuevos dos en las tablas:__

    ```bash
    Sesion-02/Ejemplo-07 $ python lista-registros.py Libro

    Tabla: Libro
    ------------
    Id | Titulo                                  | Editorial         | Numpag | Autores
     1 | Yo, Robot                               | Gnome Press       |    374 |       1
     2 | El fin de la eternidad                  | Gnome Press       |    191 |       1
     3 | El arte de la guerra                    | Obelisco          |    112 |       2
     4 | Las Bóvedas de acero                    | Debolsillo        |    272 |       1
     5 | El sol desnudo                          | Debolsillo        |    288 |       1
     6 | Halo Mythos. Guía a la historia de Halo | Altea             |    208 |       1
     7 | Godel Escher Bach                       | Tusquets Editores |    480 |       1
     8 | El Principito                           | Emece             |    112 |       1
    ------------
    ```
    Ahora podemos usar este script para inicializar nuestras bases de datos en lugar de usar el comando con docker.
    ***

#### CASOS DE ÉXITO
En la actualizad el uso de Python para la automatización de procesos está diversificada en todo el mundo, desde adquisición de datos en sondas meteorológicas, pasando por redes, orquestación de infraestructura, movil, web, desktop hasta en áreas como educación, cine, distribución de contenido o en la astronomía.

__Referencias:__
 1. https://medium.com/netflix-techblog/python-at-netflix-bba45dae649e
 1. https://realpython.com/world-class-companies-using-python/
 1. https://www.genbeta.com/desarrollo/netflix-explica-donde-como-utiliza-python-aprendizaje-automatico-automatizacion-pasando-seguridad

`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 05`](../Readme.md) > Ejemplo-01
## Conociendo e instalando Django Rest Framework

### OBJETIVO
- Conocer Django Rest Framework
- Instalando Django Rest Framework

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-05/Ejemplo-01`
1. Activar el entorno virtual __Bedutravels__
1. __Django Rest Framework__ es un módulo construido encima de Django y simplifica la creación de un API con todos los requerimientos que una API requiere, el sitio principal es:
  - Sitio principal: http://www.django-rest-framework.org
  - Guía rápida: https://www.django-rest-framework.org/tutorial/quickstart/
  - Tutorial: https://www.django-rest-framework.org/tutorial/1-serialization/
  - Ajax, CSRF y CORS: https://www.django-rest-framework.org/topics/ajax-csrf-cors/

### DESARROLLO
1. __INSTALACIÓN__ de Django Rest Framework se realiza con el comando pip de la siguiente forma:

   ```console
   (Bedutravels) Ejemplo-01 $ pip install djangorestframework
   Collecting djangorestframework
     Downloading https://files.pythonhosted.org/packages/1b/fe/fcebec2a98fbd1548da1c12ce8d7f634a02a9cce350833fa227a625ec624/djangorestframework-3.9.4-py2.py3-none-any.whl (911kB)
        |████████████████████████████████| 921kB 249kB/s
   Installing collected packages: djangorestframework
   Successfully installed djangorestframework-3.9.4

   (Bedutravels) Ejemplo-01 $
   ```

   __Se actualiza el archivo `requeriments.txt` para incluir el módulo instalado:__

   ```console
   (Bedutravels) Ejemplo-01 $ pip freeze > requeriments.txt

   (Bedutravels) Ejemplo-01 $ cat requeriments.txt
   certifi==2019.3.9
   Django==2.2.2
   djangorestframework==3.9.4
   pytz==2019.1
   sqlparse==0.3.0

   (Bedutravels) Ejemplo-01 $
   ```

__Nota:__ Recuerda incluir el archivo `requeriments.txt` en tu repo para que ya sea tú o tú equipo pueda replicar el entorno de desarrollo y además sea homogéneo.

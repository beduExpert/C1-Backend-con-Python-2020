[`Backend con Python`](../../Readme.md) > [`Sesión 08`](../Readme.md) > Ejemplo-03
## Prueba de Formularios

### OBJETIVOS
- Crear pruebas para Formularios

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-08/Ejemplo-03`

### DESARROLLO

1. Crear un entorno virtual para el proyecto **django-locallibrary-tutorial** con Django usando el siguiente comando:

`conda create --name django-locallibrary-tutorial python=3.7`

![](img/1.jpeg)

2. Activaremos el entorno virtual con el comando:

	`conda activate django-locallibrary-tutorial`

1. Entramos al directorio django-locallibrary-tutorial**

	`cd django-locallibrary-tutorial`

1. Instalaremos los requerimientos del archivo requirements.txt y procederemos a realizar las migraciones y crear el super usuario con los siguientes comandos:**

   ```
   pip3 install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py collectstatic
   python3 manage.py createsuperuser
   python3 manage.py runserver
   ```
![](img/2.jpeg)

### Pruebas en formularios

1. La filosofía para probar sus formularios es la misma que para probar sus modelos; debe probar todo lo que haya codificado o su diseño especifique, pero no el comportamiento del marco subyacente y otras bibliotecas de terceros.

	Generalmente, esto significa que debe probar que los formularios tengan los campos que desea y que estos se muestren con las etiquetas y el texto de ayuda adecuados. No es necesario que verifique que Django valida el tipo de campo correctamente (a menos que haya creado su propio campo personalizado y validación), es decir, no necesita probar que un campo de correo electrónico solo acepta correos electrónicos. Sin embargo, necesitaría probar cualquier validación adicional que espera que se realice en los campos y cualquier mensaje que su código genere para detectar errores.
	
	Considere nuestra forma de renovar libros. Esto solo tiene un campo para la fecha de renovación, que tendrá una etiqueta y un texto de ayuda que necesitaremos verificar.

	```python
	class RenewBookForm(forms.Form):
	    """
	    Form for a librarian to renew books.
	    """
	    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
	
	    def clean_renewal_date(self):
	        data = self.cleaned_data['renewal_date']
	
	        #Check date is not in past.
	        if data < datetime.date.today():
	            raise ValidationError(_('Invalid date - renewal in past'))
	        #Check date is in range librarian allowed to change (+4 weeks)
	        if data > datetime.date.today() + datetime.timedelta(weeks=4):
	            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
	
	        # Remember to always return the cleaned data.
	        return data
```

1. Abra el archivo **/catalog/tests/test_forms.py** y reemplace cualquier código existente con el siguiente código de prueba para el `RenewBookForm` formulario. Comenzamos importando nuestro formulario y algunas bibliotecas de Python y Django para ayudar a probar la funcionalidad relacionada con el tiempo de prueba. Luego declaramos nuestra clase de prueba de formulario de la misma manera que lo hicimos para los modelos, usando un nombre descriptivo para nuestra `TestCase` clase de prueba derivada.

	```python
	from django.test import TestCase
	
	# Create your tests here.
	
	import datetime
	from django.utils import timezone
	from catalog.forms import RenewBookForm
	
	class RenewBookFormTest(TestCase):
	
	    def test_renew_form_date_field_label(self):
	        form = RenewBookForm()        
	        self.assertTrue(form.fields['renewal_date'].label == None or form.fields['renewal_date'].label == 'renewal date')
	
	    def test_renew_form_date_field_help_text(self):
	        form = RenewBookForm()
	        self.assertEqual(form.fields['renewal_date'].help_text,'Enter a date between now and 4 weeks (default 3).')
	
	    def test_renew_form_date_in_past(self):
	        date = datetime.date.today() - datetime.timedelta(days=1)
	        form_data = {'renewal_date': date}
	        form = RenewBookForm(data=form_data)
	        self.assertFalse(form.is_valid())
	
	    def test_renew_form_date_too_far_in_future(self):
	        date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
	        form_data = {'renewal_date': date}
	        form = RenewBookForm(data=form_data)
	        self.assertFalse(form.is_valid())
	
	    def test_renew_form_date_today(self):
	        date = datetime.date.today()
	        form_data = {'renewal_date': date}
	        form = RenewBookForm(data=form_data)
	        self.assertTrue(form.is_valid())
	        
	    def test_renew_form_date_max(self):
	        date = timezone.now() + datetime.timedelta(weeks=4)
	        form_data = {'renewal_date': date}
	        form = RenewBookForm(data=form_data)
	        self.assertTrue(form.is_valid())
	```

1. Las dos primeras funciones prueban que los campos `label` y `help_text` son los esperados. Tenemos que acceder al campo utilizando el diccionario de campos (por ejemplo `form.fields['renewal_date'`]). Tenga en cuenta aquí que también tenemos que probar si el valor de la etiqueta es `None`, porque aunque Django representará la etiqueta correcta, devuelve `None` si el valor no está establecido explícitamente .

	El resto de las funciones prueban que el formulario es válido para fechas de renovación que están dentro del rango aceptable y no válido para valores fuera del rango. Observe cómo construimos valores de fecha de prueba alrededor de nuestra fecha actual (`datetime.date.today()`) usando `datetime.timedelta()`(en este caso especificando un número de días o semanas). Luego, simplemente creamos el formulario, pasamos nuestros datos y probamos si es válido.
	
	> Nota: Aquí no usamos la base de datos o el cliente de prueba. Considere modificar estas pruebas para usar SimpleTestCase .
	
	> También necesitamos validar que se generan los errores correctos si el formulario no es válido; sin embargo, esto generalmente se hace como parte del procesamiento de la vista, por lo que nos ocuparemos de eso en la siguiente sección.

1. Eso es todo por las formas; tenemos algunos otros, pero son creados automáticamente por nuestras vistas de edición genéricas basadas en clases, ¡y deberían probarse allí! ¡Ejecute las pruebas y confirme que nuestro código aún pasa!

```console
python3 manage.py test
```

![](img/3.png)

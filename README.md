Instrucciones formales para ejecutar la aplicación (Windows — PowerShell)

A continuación se describen las instrucciones precisas y mínimas para ejecutar localmente el servidor de desarrollo de esta aplicación Django. Este proyecto utiliza una base de datos externa que se proporcionará por separado; por tanto, será necesario indicar sus credenciales y parámetros en `proyectoHotel/settings.py`.

Requisitos previos:
- Python 3.8 o superior instalado y accesible desde PowerShell (`python --version`).

Procedimiento:

1) Abra PowerShell y sitúese en la carpeta que contiene `manage.py`.

```powershell
cd .\proyectoHotel
# Alternativamente use la ruta absoluta, por ejemplo:
# cd "C:\Users\SuUsuario\Ruta\al\repositorio\proyectoHotel"
```

2) Configure la conexión a la base de datos externa.

	Se puede proceder de dos formas:

	a) Editar directamente `proyectoHotel/settings.py` y ajustar la sección DATABASES con las credenciales proporcionadas (host, puerto, usuario, contraseña, nombre de la base de datos y driver).

	b) Crear un archivo local de configuración (por ejemplo `local_settings.py`) que contenga la configuración de `DATABASES` y modificar `settings.py` para importarlo si existe. El archivo con las credenciales no debe incluirse en el control de versiones.

3) Aplique migraciones de la aplicación (esto es necesario para crear tablas vacías o actualizar esquema si procede):

```powershell
python manage.py migrate
```

4) Inicie el servidor de desarrollo:

```powershell
python manage.py runserver
```

6) Abra un navegador y acceda a la aplicación en:

http://127.0.0.1:8000/

Observaciones y resolución de problemas comunes:
- Si PowerShell no reconoce `python`, confirme que Python está instalado y agregado al PATH.
- Si `manage.py` no se encuentra en la carpeta actual, verifique la ubicación y sitúese en la carpeta correcta antes de ejecutar los comandos.
- Si el proyecto está configurado para una base de datos distinta (por ejemplo MySQL o PostgreSQL), será necesario instalar los controladores correspondientes y ajustar `proyectoHotel/settings.py`.

Instrucciones específicas para MySQL
---------------------------------
Instale:

`mysqlclient`:

Ejemplo de configuración `DATABASES` en `proyectoHotel/settings.py` (MySQL):

```python
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'nombre_basedatos',
		'USER': 'usuario',
		'PASSWORD': 'contraseña',
		'HOST': 'direccion_host',  # ej. '127.0.0.1' o IP remota
		'PORT': '3306',
	}
}
```


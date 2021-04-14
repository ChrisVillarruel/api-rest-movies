# Django Rest Framework - Reseñas de Peliculas

Aplicación web API para la creación de reseñas de peliculas. Cada reseña va estar relacionada al usuario que realizo la reseña.

### Instalación.

##### Requerimientos Externos:
- Gestor de base de datos Realcional o no Relacional.
- Python 3.6 en adelante.
- Manejo de paquetes PIP ¡actualizado!.
- Editor de codigo, el que usted guste.
- Herramienta para la comunicación HTTP postman.

##### Pasos para utililizar la aplicación de manera local.

Clonamos el repositorio dentro de un directorio.
```sh
$ git clone https://github.com/ChrisVillarruel/api-rest-movies.git
```

Creamos un entorno virtual.
- Windows 
```sh
$ python -m venv nombre_entorno
$ cd nombre_entorno
$ cd Scripts/activate
```
- GNU Linux
```sh
$ python3 -m venv nombre_entorno
$ cd nombre_entorno
$ source bin/activate
```

Instalamos dependencias

```sh
# actualizamos pip
$ python.exe -m pip install --upgrade pip

# Dentro del repositorio master* instalamos las dependencias
$ pip install -r requirements.txt
```

Abrimos el repositorio con editor de codigo y nos dirigimos: config/settigs/base.py

```sh
# config/settigs/base.py
Borramos la importación: from . import database_info

# Configuramos nuestra base de datos.
ENGINE = 'django.db.backends.mysql'
NAME_SCHEMA = database_info.NAME_SCHEMA
USERNAME = database_info.USERNAME
PASSWORD = database_info.PASSWORD
HOST = database_info.HOST
PORT = database_info.PORT
```

Para finalizar realizamos migraciones:
```sh
# dentro del modulo raiz de api_rest_movies ejecutamos.
$ python manage.py migrate

# Levantamos el servidor
$ python manage.py runserver
```



## Actualización | Hace 2 meses.

- Creación de la entidad clasificación.
- Creacion de la entidad categoria para una pelicula.
- Creación de la entidad pelicula.
- Serialización para cada controlador.
- Controladores para cada entidad.
- Manejor local de URLS para cada controlador.
- Validaciones de datos entre la capa del modelado y serializadores de django REST

## Actualización | Domingo 14 de marzo 2021.

Se actualizo casi todo el codigo fuente.

- Modelos relacionales serializados. 
- Las vistas ahora trabajan con ViewSets.
- Implementación de routers.
- Serializadores mas robustos.
- Manejo de excepciones mas robusto.
- Fichero de dependencias.
- Elimincación logica de recursos

## Actualización | Martes 16 de marzo 2021.

Se implemento la paginación en los listados de recursos.

- Paginación del ViewSet CategoryMovies y Movies.


## Actualización | Martes 13 de abril 2021.

Al clonar este repositorio, la configuración de la base de datos sera mas sencilla.

- Posibilidad de configurar una base de datos en cualquier plataforma, Windows, IOS, GNU Linux.




# Diagrama Entidad Relación 

![This is a alt text.](/images_github/mer.png "This is a sample image.")


# De las entidades creadas se demostrara el funcionamiento de la entitad Movies.
### Listado de una pelicula.
- http://example_name_domain.com/movies/api/
- Me retorna todas las peliculas de la base de datos utilizando el metodo get.  

![This is a alt text.](/images_github/list_movies.png "This is a sample image.")

### Detallado de una pelicula
- http://example_name_domain.com/movies/api/4
- Igreso el numero de ID de la pelicula que quiero detallar y me mostrara el detalle de la pelicula al igual que los datos que se relacionan con ella utilizando el meotod get mas un id.

![This is a alt text.](/images_github/detail_movie.png "This is a sample image.")

### Creación de una pelicula
- http://example_name_domain.com/movies/api/
- Creación de una pelicula utilizando el metodo POST.
- Me retorna un mensaje de exitoso, con el nombre de la pelicula que se creo.

![This is a alt text.](/images_github/post_movie.png "This is a sample image.")

### Actualización de una pelicula
- http://example_name_domain.com/movies/api/3
- Actualizamos una pelicula con el metodo PUT.
- Me retorna un mensaje de exitoso, con el nombre de la pelicula que se actualizo.

![This is a alt text.](/images_github/put_movie.png "This is a sample image.")

### Actualización Parcial de una pelicula.
- http://example_name_domain.com/movies/api/3
- Actualizamos una pelicula de forma parcial utilizando el metodo PATCH.
- Me retorna un mensaje de exitoso, con el nombre de la pelicula que se actualizo.

![This is a alt text.](/images_github/patch_movie.png "This is a sample image.")

### Eliminar Pelicula.
- http://example_name_domain.com/movies/api/1
- Eliminamos una pelicula con el metodo DELETE.
- Me retorna un mensaje de exitoso, con el nombre de la pelicula que se elimino.

![This is a alt text.](/images_github/delete_movie.png "This is a sample image.")

### Error 404 No encontrado..
- http://example_name_domain.com/movies/api/120
- Este tipo de error solo funciona para la busqueda de recursos que no existan en la base de datos.
- Los errores como nombres de modulos incorrectos aun se sigue desarronllando un metodo que permita retornar al usuario el mismo error.
- Me retorna un mensaje de error 404.

![This is a alt text.](/images_github/error_not_found.png "This is a sample image.")

### Error 400 Errores de validación de campos.
- http://example_name_domain.com/movies/api/120
- Este tipo de error se dispara cuando un dato no concuerda con lo esperador.
- Los errores como nombres de modulos incorrectos aun se sigue desarronllando un metodo que permita retornar al usuario el mismo error.
- Me retorna un mensaje de error 400 con los errores mas detallados.

![This is a alt text.](/images_github/error_validations.png "This is a sample image.")



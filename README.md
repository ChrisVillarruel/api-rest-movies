# Actualmente la aplicación sigue en desarrollo

## ¿Actualmente que esta haciendo la aplicación?

- Creación de la entidad clasficiación.
- Creacion de la entidad categoria para una pelicula.
- Creación de la entidad pelicula.
- Serializadores para cada entidad.
- Controladores para cada entidad.
- Manejor local de URLS para cada controlador.
- Validaciones de datos entre la capa del modelado y serializadores de django REST
- Creación, Listado, Actualización, Actualización parcial y eliminación de regsitros para cada entidad.
- Manejo de errores 400.

## ¿Que le falta a la aplicación para ser terminada?

- Control de errores del Servidor (+500).
- Sesiones.
- Tokens de autenticación utilizando la libreria pyjwt de (JSON WEB TOKEN)
- Paginación de datos.
- Activación de cuentas.
- Verificación de cuentas.
- Inicio de sesión de terceros (Google, Facebook, Twitter )
- Permisos Mixin.
- Entidad reseñas.


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



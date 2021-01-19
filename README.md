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
- Me retorna todas las peliculas de la base de datos.  

![This is a alt text.](/images_github/list_movies.png "This is a sample image.")

### Detallado de una pelicula
- http://example_name_domain.com/movies/api/4
- Igreso el numero de ID de la pelicula que quiero detallar y me mostrara el detalle de la pelicula al igual que los datos que se relacionan con ella.

![This is a alt text.](/images_github/detail_movie.png "This is a sample image.")




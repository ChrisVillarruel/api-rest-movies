from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    # Paginación corta

    # Numeros de recursos por defecto de un listado
    page_size = 5

    # Parametro que hace referencia al numero de pagina
    page_query_param = 'page'

    # Parametro que hace refrencia al filtrado de datos que se desee listar
    page_size_query_param = 'filter'

    # Numero maximo de paginación
    max_page_size = 1000

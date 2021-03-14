from datetime import datetime


def msg_error(message, code, detail=None):
    if detail is None:
        detail = 'Error no detallado'

    msg_error = {
        'error': {
            'message': message,
            'code': code,
            'details': detail
        }
    }
    return msg_error


def base_resource(message, code):
    return {
        'detail': message,
        'status_code': code
    }


def resource_created():
    created = base_resource(message='Recurso Creado.', code=201)
    return created


def resource_updated():
    update = base_resource(message='Recurso Actualizado.', code=200)
    return update


def resource_destroy():
    destroy = base_resource(message='Recurso Eliminado.', code=200)
    return destroy


def not_found():
    not_found = base_resource(message='No encontrado.', code=404)
    return not_found

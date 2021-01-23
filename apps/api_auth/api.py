from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime

from .serializers import UserSerializer


def msg_error(message, status, code, detail=None):
    if detail is None:
        detail = 'Error no detallado'

    msg_error = {
        'error': {
            'message': message,
            'status': status,
            'code': code,
            'date': datetime.now().strftime("%d-%m-%Y"),
            'details': detail
        }
    }
    return msg_error


class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            msg_success = {
                'success': 'Usuario creado exitosamente'}
            return Response(msg_success, status=status.HTTP_201_CREATED)

        error = msg_error('Error de validación', 'BAD_REQUEST', 400, serializer.errors)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

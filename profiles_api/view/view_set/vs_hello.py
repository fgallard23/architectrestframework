from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api.serializer.api_view import sv_hello


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = sv_hello.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps URLs using Routers',
            'Provides more functionality with less code'
        ]
        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)  # valid trama de entrada

        if serializer.is_valid():
            name = serializer.validated_data.get('name')  # get input parameter
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """handle updating object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """handle updating part of object"""
        return Response({'http_method': 'PATCH'})

    def delete(self, request, pk=None):
        """handle removing of object"""
        return Response({'http_method': 'DELETE'})

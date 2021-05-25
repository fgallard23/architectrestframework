from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from profiles_api.serializer.api_view import sv_hello


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = sv_hello.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data) # valid trama de entrada

        if serializer.is_valid(): # valid input
            name = serializer.validated_data.get('name') # get input parameter
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # replace all object
    def put(self, request, pk=None): # pk object id for updating
        """Handle updating object"""
        return Response({'method':'PUT'})

    # replace fields object
    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
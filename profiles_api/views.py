from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View."""

    def get(self, request, format=None):
        """Return a list of APIView Features"""
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'Is similar to a traditional DJango View',
            'Gives you the most control over your application loogic',
            'Is mapped manually to the URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})

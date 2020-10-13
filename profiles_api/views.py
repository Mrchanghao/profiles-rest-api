from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    '''
    test api view
    '''
    def get(self, request, format=None):
        """ return a list of APIVIEW features """
        an_apiview = [
            'uses http methods as function (get, post, patch , put, delete)',
            '유사한 장고 view',
            'gives you the most control over tou app logic',
            'is mapped manually to urls',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

# Create your views here.

class HelloApiView(APIView):
    '''
    test api view
    '''
    # serializers 에서 작성한 클래스를 가져와서 이용
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """ return a list of APIVIEW features """
        an_apiview = [
            'uses http methods as function (get, post, patch , put, delete)',
            '유사한 장고 view',
            'gives you the most control over tou app logic',
            'is mapped manually to urls',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        '''
        create a hello message with our name
        :param request:
        :return:s
        '''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
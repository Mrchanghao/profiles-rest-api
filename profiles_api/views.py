from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
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
            message = f'안녕하십니끼??? {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        '''
        put method
        pk --> primary key
        :param request:
        :return: response
        Handle update object
        '''
        return Response({'Method': 'PUT'})

    def patch(self, request, pk=None):
        '''

        :param request:
        :param pk:
        :return:
        '''
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        '''
        delete request
        :param request:
        :param pk:
        :return:
        '''
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    '''
    test api viewset
    '''
    def list(self, request):
        '''
        :param request:
        :return: a hello message
        '''
        a_viewset = [
            'Users actions (list, create, retrieve, update, partial_update)',
            '자동 map url using routers',
            '적은 코드로 많은 기능 제공'
        ]
        return Response({'message': 'hello', 'a view_set': a_viewset})

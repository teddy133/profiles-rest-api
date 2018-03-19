from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets

# Create your views here.

from rest_framework.response import Response
from . import serializers
from rest_framework import status


class HelloApiView(APIView):
    '''test an Api'''

    serializer_class = serializers.HelloSerializer

    def post(self, request):
        '''create a hello messgae with the name returned'''
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message' : message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, format=None):
        '''returns a list of ApiView Features'''

        an_apiview = [
            '''uses http methods as functions'''

        ]
        return Response({'message' : 'hello', 'ApiView': an_apiview})


    def put(self, request,pk=None):
        'handles updating an object'
        return Response({'method': 'put'})
    def patch(self, request, pk=None):
        'patch request only updates fileds provided in the request'
        return Response({'method': 'patch'})
    def delete(self, request, pk=None):
        'delete an object'
        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    '''Test Api ViewSet'''
    def list(self, request):
        '''return a hello message'''

        a_viewset = [
            'Uses actions (list, ceate, retrieve, update, partial_update)',
            'automaticall maps to urls using routers.',
            'provides more functionality with less code.'
        ]
        return Response({'message': 'Hello', 'a_viewset': a_viewset})

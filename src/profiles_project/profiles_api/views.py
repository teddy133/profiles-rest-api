from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets

# Create your views here.

from rest_framework.response import Response
from . import serializers
from rest_framework import status
from . import models
from . import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters


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
    serializer_class = serializers.HelloSerializer

    def create(self, request):
        '''Create  a new hello message'''
        serialzer = serializers.HelloSerializer(data=request.data)

        if serialzer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'Custom message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        '''handles getting an object by its id'''
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        '''handles updaate object'''
        return Response({'http_method': 'PUT'})
    def partial_update(self, request, pk=None):
        '''handles update part of pbject'''
        return Response({'http_method': 'Update'})

    def destroy(self, request, pk=None):
        return({'http_method': 'Destroy'})

    def list(self, request):
        '''return a hello message'''

        a_viewset = [
            'Uses actions (list, ceate, retrieve, update, partial_update)',
            'automaticall maps to urls using routers.',
            'provides more functionality with less code.'
        ]
        return Response({'message': 'Hello', 'a_viewset': a_viewset})

class userProfileViewSet(viewsets.ModelViewSet):
    '''handles cerating , and updating a profile'''
    serializer_class = serializers.userProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes =(permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
    

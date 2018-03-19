from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.

from rest_framework.response import Response



class HelloApiView(APIView):
    '''test an Api'''

    def get(self, request, format=None):
        '''returns a list of ApiView Features'''

        an_apiview = [
            '''uses http methods as functions'''

        ]
        return Response({'message' : 'hello', 'ApiView': an_apiview})

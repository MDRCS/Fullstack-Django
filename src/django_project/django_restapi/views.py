from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIVIEW(APIView):

    def get(self, request, format=None):
        users = ['Mohamed El Rahali',
                 'Anas Eit Lhioui']

        return Response({'message': 'hello', 'users': users})

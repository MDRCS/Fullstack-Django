from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # http status
from . import serializers


class HelloAPIVIEW(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        users = ['Mohamed El Rahali',
                 'Anas Eit Lhioui']

        return Response({'message': 'hello', 'users': users})

    def post(self, request):
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hellow {0}'.format(name)
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        return Response({'method': 'put'})

    def patch(self, request):
        return Response({'method': 'patch'})

    def delete(self, request):
        return Response({'method': 'delete'})

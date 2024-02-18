from django.shortcuts import render
from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class AliveView(generics.GenericAPIView):
    http_method_names = ['get']

    def get(self, request):
        return Response({'status':'ok'}, status=status.HTTP_200_OK)
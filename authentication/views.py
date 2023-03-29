from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,APIView
from rest_framework import generics

# Create your views here.


class AuthView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={'message':'hello'},status=status.HTTP_200_OK)
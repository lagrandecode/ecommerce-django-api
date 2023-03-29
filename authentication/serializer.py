from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,APIView
from .models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'




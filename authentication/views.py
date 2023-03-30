from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,APIView
from rest_framework import generics
from .serializer import CustomerSerializer
from .models import Customer

# Create your views here.


class CustomerView(APIView):
    def get(self,request,format=None):
        customers = Customer.objects.all()
        serializers = CustomerSerializer(customers,many=True)
        return Response(serializers.data)
    
    def post(self,request,format=None):
        customer = Customer.objects.all()
        serializers = CustomerSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
#-------------------------------------------------------------------------------------------

# This code is to show the count of customer in the admin portal 

#-------------------------------------------------------------------------------------------
    
def home(request):
    customer = Customer.objects.all().count()
    context = {
        'customer':customer
    }
    return render(request,'home.html',context)


#-------------------------------------------------------------------------------------------
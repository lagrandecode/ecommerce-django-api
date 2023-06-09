from django.db import models
from django.utils.timezone import datetime
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=14)
    email = models.EmailField()
    profile_pics = models.ImageField(upload_to='images/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


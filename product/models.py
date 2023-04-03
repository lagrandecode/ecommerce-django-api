from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    price = models.PositiveIntegerField()
    product_images = models.ImageField(upload_to='images/')
    promo_price = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    PRODUCT_SIZE=(
        ('Small','Small'),
        ('Large','Large'),
        ('Extra Large','Extra Large'),
    )
    size = models.CharField(max_length=20,choices=PRODUCT_SIZE)
    PRODUCT_STATUS = (
        ('Pending','Pending'),
        ('Order Confirm','Order Confirm'),
        ('Out of Delivery','Out of Delivery'),
        ('Delivery','Delivery'),
    )
    status = models.CharField(max_length=20,choices=PRODUCT_STATUS)

    def __str__(self):
        return self.product_name

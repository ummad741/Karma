from django.db import models
from Admins.models import Admin

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    image = models.ImageField(upload_to='product-image/')
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'name: {self.name} | price: {self.price} | admin: {self.admin}'
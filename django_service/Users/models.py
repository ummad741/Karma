from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone_regex = RegexValidator(
        regex='d{0,9}', message="Telefon raqamini +998xxxxxxxxx kabi kriting")
    phone = models.CharField(
        validators=[phone_regex], max_length=9, unique=True
    )
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_login_date = models.DateTimeField(null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to='user-profile/', null=True, blank=True)

    def __str__(self):
        return f"id: {self.pk} | name: {self.name}"

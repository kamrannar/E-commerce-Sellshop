from django.db import models
from django.contrib.auth.models import AbstractUser
from product.models import Product_version

COUNTRY_CHOICES = (
    ('AZ', 'Azerbaijan'),
    ('AR', 'Armenia'),
    ('GE', 'Georgia')
)

CITY_CHOICES = (
    ('BA', 'Baku'),
    ('YR', 'Yerevan'),
    ('TB', 'Tbilisi')
)


class User(AbstractUser):
    phone = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    additional_info = models.TextField()
    street = models.CharField(max_length=250)
    country = models.CharField(choices=COUNTRY_CHOICES, max_length=2)
    city = models.CharField(choices=CITY_CHOICES, max_length=2)

    def __str__(self):
        return f'{self.id} - {self.username}'


class Wishlist(models.Model):
    product_version_id = models.ForeignKey(
        Product_version, on_delete=models.CASCADE, null=True)
    user_id_wishlist = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} -    {self.product_version_id}'


class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} -    {self.user_id.username}'


class Cart_item(models.Model):
    product_version_id = models.ForeignKey(
        Product_version, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.id} -    {self.product_version_id}'


class Newsletter(models.Model):
    emails = models.EmailField(unique=True)

    def __str__(self):
        return self.emails
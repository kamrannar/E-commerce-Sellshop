from accounts.models import User
from django.db import models
from product.models import Product_version


class Wishlists(models.Model):
    product_version_id = models.ForeignKey(
        Product_version, on_delete=models.CASCADE,null=True)
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

class Cart_items(models.Model):
    product_version_id = models.ForeignKey(
        Product_version, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.id} -    {self.product_version_id}'
from django.db import models
from django.contrib.auth.models import AbstractUser
import redis


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


class Billing(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    country = models.CharField(choices=COUNTRY_CHOICES, max_length=2)
    city = models.CharField(choices=CITY_CHOICES, max_length=2)
    street = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.first_name} -    {self.last_name}'


class Different_shipping(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    country = models.CharField(choices=COUNTRY_CHOICES, max_length=2)
    city = models.CharField(choices=CITY_CHOICES, max_length=2)
    street = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.first_name} -    {self.last_name}'


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

class Newsletter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self) :
        return self.email

    # def save(self,*args,**kwargs):
    #     super(Newsletter,self).save(*args,**kwargs)
    #     print(self.email)
    #     r=redis.Redis(host='localhost',port=6379)
    #     r.publish('email_channel',self.email)
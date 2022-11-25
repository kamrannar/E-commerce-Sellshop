from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator


class Brand(models.Model):
    brands = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.brands}'


class Category(models.Model):
    categories = models.CharField(max_length=250)
    subcategories = models.ForeignKey("Category",on_delete=models.CASCADE, null=True, blank=True ) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.categories}  '


class Color(models.Model):
    colors = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.colors}'


class Size(models.Model):
    sizes = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.sizes}'



class Product(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    category_id =models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    product_size = models.ManyToManyField(Size)
    product_color = models.ManyToManyField(Color)
    cover_image = models.ImageField(
        upload_to="Cover_images", unique=True, null=True)
    def __str__(self):
        return f' {self.title} '
    
class Product_version(models.Model):
    name = models.CharField(max_length = 100)
    color_id = models.ForeignKey(Color, on_delete=models.CASCADE, null=True,related_name='color_id')
    size_id = models.ManyToManyField(Size)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField()
    stocks = models.IntegerField(validators=[MinValueValidator(1)])
    discount_price = models.FloatField(max_length=250)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,related_name='pro')
    cover_image_version = models.ImageField(
        upload_to="Cover_images_version", unique=True, null=True)
    slug = models.SlugField(max_length=120, null=True, blank=True)
    more_info = models.TextField() 
    text = models.TextField()
    product_view = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.product} {self.id}'

    def save(self, *args, **kwargs):
        value = self.product,self.id
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Image(models.Model):
    images = models.ImageField(
        upload_to="Images_images", unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_image = models.ForeignKey(
        Product_version, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.product_image}'


class Review(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review = models.CharField(max_length=250)
    products_id = models.ForeignKey(
        Product_version, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f' {self.name}'


class Collection(models.Model):
    titles = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.titles}'

class Tag(models.Model):
    name = models.CharField(max_length=100)
    tags = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
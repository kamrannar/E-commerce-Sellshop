from django.db import models
from product.models import Category
from django.utils.text import slugify
from product.models import Tag


class Blog(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    def __str__(self):
        return f'{self.id} -    {self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)


class Comments(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    blog_id = models.ForeignKey(
        Blog, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.id} -    {self.name}'


class BlogStatistic(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    read_count = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'{self.blog}'

class BlockedIP(models.Model):
    ip_addr = models.CharField(max_length=30)

    def __str__(self):
        return self.ip_addr
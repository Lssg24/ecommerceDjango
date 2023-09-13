from django.db import models
from django.urls import reverse

from category.models import Category


# Create your models here.
class Product(models.Model):
    produc_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='pothos/products')
    stock = models.IntegerField()
    is_avalible = models.BooleanField(default=True)
    # el producto se relaciona con la categoria, con las opciones otorgadas si se elimina una categoria se eliminan los productos relacionados a la categoria. por esto tambien se debe inportar la categoria.
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.produc_name

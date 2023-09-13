from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display= ('produc_name', 'price', 'stock', 'category', 'modified_date', 'is_avalible')
    prepopulated_fields=  {'slug':('produc_name',)}

#aqui registramos la identidad
admin.site.register(Product, ProductAdmin)

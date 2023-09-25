from django.contrib import admin
from .models import Product, Variation


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('produc_name', 'price', 'stock', 'category', 'modified_date', 'is_avalible')
    prepopulated_fields = {'slug': ('produc_name',)}


# esto solo funciona como vista en la administracion de django.
class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variations_category', 'variations_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variations_category', 'variations_value', 'is_active')


# aqui registramos la identidad
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)

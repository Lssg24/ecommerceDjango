from django.urls import path
from . import views


# urlpatterns es para listar las rutas de las vistas
urlpatterns = [
    path('', views.store, name="store"),
    path('<slug:category_slug>', views.store, name='poducts_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',
         views.product_detail, name='product_detail'),
]

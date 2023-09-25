from django.urls import path
from . import views


# urlpatterns es para listar las rutas de las vistas
urlpatterns = [
    path('', views.store, name="store"),
    path('category/<slug:category_slug>', views.store, name='poducts_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/',
         views.product_detail, name='product_detail'),
    path('search/', views.search, name='search',)
]

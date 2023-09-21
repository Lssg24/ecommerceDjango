from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from carts.models import CartItem
from carts.views import _cart_id
# Quiero hacer una consulta a la base de datos es por esto que debo importar el modelo que necesito
from .models import Product

from category.models import Category


# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=categories, is_avalible=True)
        paginator = Paginator(products,1)
        page =request.GET.get('page')
        page_product = paginator.get_page(page)
        product_count = products.count
    else:
        products = Product.objects.all().filter(is_avalible=True)
        # para paginar la catidad de objetos que quiero mostrar en una pagina
        paginator = Paginator(products,1)
        page =request.GET.get('page')
        page_product = paginator.get_page(page)

        product_count = products.count

    context = {
        'products': page_product,
        'product_count': product_count,

    }

    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product. objects.get(
            category__slug=category_slug, slug=product_slug)
        # category__slug lo utilizaremos para traer el dato slug que compararemos.
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()#para obtener una propiedad del cartitem ponemos cart__ luego la propiedad.
    except Exception as e:
        raise e
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }

    return render(request, 'store/product_detail.html', context)

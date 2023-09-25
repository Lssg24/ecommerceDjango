from django.shortcuts import redirect, render, get_object_or_404
from store.models import Product, Variation
from . models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

# funcion para el carrito quede en la sesion del usuario


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    product_variation = []

    if request.method == 'POST':
        for item in request.POST:
            key = item
            value = request.POST[key]

            try:
                variation = Variation.objects.get(product=product, variations_category__iexact=key, variations_value__iexact=value)
                product_variation.append(variation)
            except:
                pass

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        Cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if len(product_variation) > 0 :
            cart_item.variations.clear()
            for item in product_variation:
                cart_item.variations.add(item)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        if len(product_variation) > 0 :
            for item in product_variation:
                cart_item.variations.add(item)
        cart_item.save()
    return redirect('cart')

def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))#primero instanciar el objeto carito
    product = get_object_or_404(Product, id=product_id)#instanciar el objeto producto, importar la funcion 404
    cart_item = CartItem.objects.get(product=product, cart=cart) #consultar el cart item
    if (cart_item.quantity>1):
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))  # primero instanciar el objeto carito
    product = get_object_or_404(Product, id=product_id)  # instanciar el objeto producto, importar la funcion 404
    cart_item = CartItem.objects.get(product=product, cart=cart)  # consultar el cart item
    cart_item.delete()
    return redirect('cart')



def cart(request, total=0, quantity=0, cart_items=None):
    tax = 0
    grand_total = 0
    # primero evaluamos si el producto existe en la base de datos
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_activate=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2*total)/100
        grand_total = total+tax
    except ObjectDoesNotExist:
        pass
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,

    }

    return render(request, 'store/cart.html', context)

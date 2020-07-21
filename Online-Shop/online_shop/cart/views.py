from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST
from .forms import CartAddProductForm
from .cart import Cart
from shop.models import Product
from coupons.forms import CouponForm


@require_POST
def CartAddProduct(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request=request)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product, quantity=cd['quantity'], override_quantity=cd['override'])

    return redirect('cart:cart_detail')


@require_POST
def CartRemoveProduct(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)

    return redirect('cart:cart_detail')


def CartProductsDetail(request):
    cart = Cart(request)

    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})

    coupon_apply_form = CouponForm()
    context = {'cart': cart, 'coupon_apply_form': coupon_apply_form}
    return render(request, 'cart/detail.html', context)

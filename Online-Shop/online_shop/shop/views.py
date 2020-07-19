from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }

    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    """ The 'product_detail' view expects the id and slug parameters in order to retrieve the Product instance.
        You can get this instance just through the ID, since it's a unique attribute. However, you include the
        slug in the URL to build SEO-friendly URLs for products.
    """

    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm(request.POST)
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }

    return render(request, 'shop/product/detail.html', context)

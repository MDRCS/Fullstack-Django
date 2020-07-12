from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from . import models


def productlist(request, category_slug=None):
    category = None
    productlist = models.Product.objects.all()

    if category_slug:
        category = get_object_or_404(models.Category,slug=category_slug)
        productlist = productlist.filter(category=category)
    search_query = request.GET.get('q')

    if search_query:
        productlist = productlist.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(condition__icontains=search_query) |
            Q(brand__name__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )

    category_list = models.Category.objects.annotate(total_products=Count('product'))
    paginator = Paginator(productlist, 1)
    page = request.GET.get('page')
    productlist = paginator.get_page(page)
    context = {'product_list': productlist, 'category_list': category_list, 'category': category}
    template = 'product/product_list.html'
    return render(request, template, context)


def productdetail(request, product_slug):
    product_detail = get_object_or_404(models.Product,slug=product_slug)
    product_images = models.ProductImages.objects.filter(product=product_detail)
    context = {'product_detail': product_detail, 'product_images': product_images}
    template = 'product/product_detail.html'
    return render(request, template, context)

from django.shortcuts import render, get_object_or_404
from .models import Category, Products
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.

def allProdCat(request, cslug=None):
    cpage = None
    products_list = None
    if cslug != None:
        cpage = get_object_or_404(Category, cslug=cslug)
        products_list = Products.objects.all().filter(category=cpage, available=True)
    else:
        products_list = Products.objects.all().filter(available=True)
    paginator = Paginator(products_list, 3)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, 'shopApp/category.html', {'category': cpage, 'products': products})


def proDetail(request, cslug, product_slug):
    try:
        product = Products.objects.get(category__cslug=cslug, pslug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'shopApp/product.html', {'product': product})

from django.shortcuts import render
from shopApp.models import Products
from django.db.models import Q


# Create your views here.

def searchresult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Products.objects.all().filter(Q(pname__contains=query) | Q(pdescription__contains=query))
    return render(request, 'searchApp/search.html', {'query': query, 'products': products})

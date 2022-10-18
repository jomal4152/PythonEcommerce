from . import views
from django.urls import path

app_name = 'shop'

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:cslug>', views.allProdCat, name='products_by_category'),
    path('<slug:cslug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail')
]

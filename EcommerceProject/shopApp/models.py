from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    cname = models.CharField(max_length=250, unique=True)
    cslug = models.SlugField(max_length=250, unique=True)
    cdescription = models.TextField(blank=True)
    image = models.ImageField(upload_to='CategoryImages', blank=True)

    class Meta:
        ordering = ('cname',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.cname)

    def get_url(self):
        return reverse('shop:products_by_category', args=[self.cslug])


class Products(models.Model):
    pname = models.CharField(max_length=250, unique=True)
    pslug = models.SlugField(max_length=250, unique=True)
    pdescription = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pimage = models.ImageField(upload_to='ProductImages', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('pname',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.pname)

    def get_url(self):
        return reverse('shop:prodCatdetail', args=[self.category.cslug, self.pslug])
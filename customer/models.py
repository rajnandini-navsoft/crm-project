
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.



class CustomerAdd(models.Model):
    first_name = models.CharField(max_length=255,null =True,blank=True)
    middle_name = models.CharField(max_length=255,null =True,blank=True)
    last_name = models.CharField(max_length=255,null =True,blank=True)
    mobile = models.CharField(max_length=100,null =True,blank=True)
    email = models.EmailField(max_length=200,null =True,blank=True)
    address = models.CharField(max_length=255,null =True,blank=True)


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='name')
    image = models.ImageField(upload_to="categories", blank=True)
    description = models.TextField(blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='name',null=True,blank=True)
    image = models.ImageField(upload_to="products", blank=True)
    brand = models.CharField(max_length=250, blank=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    shipping = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=10, validators=[MaxValueValidator(10), MinValueValidator(1)])
    review = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.review
# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import CustomerAdd,Category, CustomerAddress,Product,Review,State

admin.site.register(CustomerAdd)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(State)
admin.site.register(CustomerAddress)
# Register your models here.

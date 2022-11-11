from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import Product, Order, Review, UserCart

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(UserCart)



admin.site.register(Session)

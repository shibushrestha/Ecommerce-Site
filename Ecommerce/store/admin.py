from django.contrib import admin
from store.models import *


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderedItem)
admin.site.register(UserProfile)

from django.db import models
from django.contrib.auth.models import User

    
# The product model
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

# This is the cart model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_total_item(self):
        ordereditem = self.ordereditem_set.all()
        total = sum([item.quantity for item in ordereditem])
        return total

    @property
    def get_cart_total(self):
        ordereditem = self.ordereditem_set.all()
        total = sum([item.get_total for item in ordereditem])
        return total

# product the customer ordered
class OrderedItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.SmallIntegerField(default=0, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
     
# shipping Info of the user
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    mobile_number = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return str(self.address)
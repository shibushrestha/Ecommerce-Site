from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


# The Product model
class Product(models.Model):
	product_name = models.CharField(max_length = 100)
	price = models.IntegerField(default = 0)
	product_image = models.ImageField(blank=True)
	date_added = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.product_name

	'''
	While this code is correct and simple, it may not be the most portable way to to write this kind of method.
	The reverse() function is usually the best approach.
	
	def get_absolute_url(self):
		return "/Myapp/%i/" % self.id
	'''
	def get_absolute_url(self):
		return reverse("Myapp:detail", kwargs={"product_id": self.id})

# User reviewing the product.
class Review(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	review = models.CharField(max_length=1000)
	

# The order users are gonna make
class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveSmallIntegerField(default=1)
	ordered_datetime = models.DateTimeField(auto_now=True)
	# Payment Choices(for now only Cash on delivery is being implemented)
	class PaymentChoice(models.TextChoices):
		CASH_ON_DELIVERY = 'C',_('Cash on delivery')
		OTHERS = 'O',_('others')
	payment_method = models.CharField(max_length=1, choices=PaymentChoice.choices, blank=True)
	# Status of the order
	class OrderStatus(models.TextChoices):
		DELIVERED = 'D',_('Delivered')
		ON_THE_WAY = 'OTW',_('On the way')
		CANCELLED = 'C',_('Cancelled')
	order_status = models.CharField(max_length=3, choices=OrderStatus.choices, blank=True)
	
	# Individual total of a product and its quantity
	@property
	def get_order_total(self):
		total = self.product.price * self.quantity
		return total

# The cart for an user	
class UserCart(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	product = models.ManyToManyField(Product, verbose_name="cart items", blank=True)
	
	@property
	def get_cart_total(self):
		total = sum([items.price for items in self.product.all()])
		return total

# This is a proxy model that deals with the orders the user made.
class UserOrder(User):
	class Meta():
		proxy = True

	# To get the total of all the orders the user made
	@property
	def get_total_of_all_orders(self):
		all_orders = self.order_set.all()
		individual_total = [order.get_order_total for order in all_orders]
		total_of_all_orders = sum(num for num in individual_total)
		return total_of_all_orders

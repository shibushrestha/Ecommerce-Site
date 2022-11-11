from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Order, UserCart
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

import json

# This is the homepage which displays all the product in the database
def home(request,):
	product_list = Product.objects.all().order_by('date_added')
	paginator = Paginator(product_list, 20)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'Myapp/home.html', {'page_obj':page_obj})

# This is the detail view of the products
def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	context = {'product':product,}
	return render(request, 'Myapp/detail.html', context)


# This view is for the order logic
@require_http_methods(["POST"])
@login_required
def order(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	if request.method == "POST":
		quantity = request.POST.get('quantity')
		context ={
			'product':product,
			'quantity':quantity,
		}
		return render(request, 'Myapp/order.html', context)
	
	
# The order conformation view
def order_confirmation(request, product_id):
	user = request.user
	product = get_object_or_404(product, pk=product_id)
	order = Order(user=user, product=product, quantity=1, payment_method='',)


# This is the cart functionality
@login_required()
def cart(request):
	user = request.user
	# Getting UserCart if its creates or create the cart
	user_cart, created = UserCart.objects.get_or_create(user=user)
	# Getting the product from the fetch api
	if request.method == 'POST':
		data = json.loads(request.body)
		product = data['productId']
		#adding the product to the user_cart
		user_cart.product.add(product)
		user_cart.save()		
		return JsonResponse('Item successfully added to cart', safe=False)
	# If the method is GET, display the cart page.
	else:
		cart_items = user.usercart.product.all()
		if cart_items.count() == 0:
			context={'no_cart_items':"No items have been added to the cart."}
		else:
			context = {'cart_items': cart_items}
		return render(request, 'Myapp/cart.html', context)

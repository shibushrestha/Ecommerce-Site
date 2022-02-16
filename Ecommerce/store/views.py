from django.http import JsonResponse
import json
from django.shortcuts import redirect, render
from .forms import UserRegisterForm

from store.models import Product, Order, OrderedItem

def store(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.ordereditem_set.all()
        cartItems = order.get_total_item
    else:
        items = []
        order = {'get_cart_total': 0, 'get_total_item': 0}
        cartItems = order['get_total_item']
    all_product = Product.objects.all()
    context = {'all_product': all_product, 'cartItems':cartItems }
    return render (request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.ordereditem_set.all()
        cartItems = order.get_total_item
    else:
        items = []
        order = {'get_cart_total': 0, 'get_total_item': 0}
        cartItems = order['get_total_item']
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render (request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.ordereditem_set.all()
        cartItems = order.get_total_item
    else:
        items = []
        order = {'get_cart_total': 0, 'get_total_item': 0}
        cartItems = order['get_total_item']
    context = {'items':items, 'order':order, 'cartItems':cartItems,}
    return render (request, 'store/checkout.html', context)


def update_cart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    user = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(user=user, complete=False)
    orderedItem, created = OrderedItem.objects.get_or_create(order=order, product=product) 

    if action == 'add':
        orderedItem.quantity = (orderedItem.quantity + 1)
    elif action == 'remove':
        orderedItem.quantity = (orderedItem.quantity - 1)
    orderedItem.save()

    if orderedItem.quantity == 0:
        orderedItem.delete()
    return JsonResponse('Items successfully added to cart', safe=False)



# This view is for the user registration.
def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'store/register.html', {'form':form})
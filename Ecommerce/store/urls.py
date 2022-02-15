from django.urls import path
from store import views as store_view
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('', store_view.store, name='store'),
    path('cart/', store_view.cart, name='cart'),
    path('checkout/', store_view.checkout, name='checkout'),
    path('updatecart/', store_view.update_cart, name='updatecart'),

    path('register/', store_view.register_user, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),
]


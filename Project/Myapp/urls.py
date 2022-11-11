from django.urls import re_path, path
from Myapp import views, useraccountviews
from Myapp.useraccountviews import UserPasswordChange, EditUserProfile
from django.contrib.auth.views import LogoutView

app_name = 'Myapp'

urlpatterns=[
	re_path(r'^$', views.home, name='home'),
	re_path(r'(?P<product_id>[\d]+)/$', views.detail, name='detail'),
	re_path(r'^order/(?P<product_id>[\d]+)/$', views.order, name='order'),
	re_path(r'^cart/$', views.cart, name='cart'),
	
	re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
	re_path(r'^(?P<user_username>[a-zA-Z0-9!@$_.]+)/$', useraccountviews.user_profile, name='userprofile'),
    re_path(r'^(?P<user_username>[a-zA-Z0-9!@$_.]+)/changepassword/$', UserPasswordChange.as_view(), name='changepassword'),
	re_path(r'^(?P<user_username>[a-zA-Z0-9!@$_.]+)/editprofile/$', EditUserProfile.as_view(), name='edit-profile'),

]
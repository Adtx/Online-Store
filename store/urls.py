from django.urls import path
from django.conf import settings
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register', views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('update_profile', views.update_profile_view, name='update_profile'),
    path('profile', views.profile_view, name='profile'),
    path(r'products/?P<ean>\d+', views.product_details_view, name='product_details'),
    path('product_search', views.product_search_view, name='product_search'),
    path('product_search/sort', views.sort_results_view, name='sort_results'),
    path('filter_results', views.filter_results_view, name='filter_results'),
    path('show_cart', views.show_cart_view, name='show_cart'),
    path('add_cart_item', views.add_cart_item_view, name='add_cart_item'),
    path('remove_cart_item', views.remove_cart_item_view, name='remove_cart_item'),
    path('update_cart_item', views.update_cart_item_view, name='update_cart_item'),
    path('checkout', views.process_payment_view, name='checkout'),
    path('purchased', views.purchased_view, name='purchased'),
    path('canceled', views.canceled_view, name='canceled'),
    path('history', views.purchase_history_view, name='history'),
    path(r'orders/?P<order_id>\d+', views.order_details_view, name='order_details'),
]

if settings.DEBUG:
   import debug_toolbar
   urlpatterns += [
       url(r'^__debug__/', include(debug_toolbar.urls)),
   ]
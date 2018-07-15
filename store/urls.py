from django.urls import path

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
]
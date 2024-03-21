from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', views.products, name='products'),
    path('filter=<str:category>', views.filter_products, name='filter_products'),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("basket/", basket_view, name="basket"),
    path("create_receipt/", create_receipt, name="create_receipt"),
    path('add_to_basket/<int:pk>', add_to_basket, name='add_to_basket'),
    path('remove_from_basket/<int:pk>', remove_from_basket, name='remove_from_basket'),
    path('remove_from_basket_products/<int:pk>', remove_from_basket_products, name='remove_from_basket_products'),
    path('create_product/', create_product, name='create_product'),
    path('update_product/<int:pk>', UpdateProduct.as_view(), name='update_product'),
    path('delete_product/<int:pk>', delete_product, name='delete_product'),
    path('update_user/<int:user_id>/', update_user, name='update_user'),
    path('product_page/<int:pk>/', product_page, name='product_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

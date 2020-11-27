from django.urls import include, path
from . import views


urlpatterns = [
    path('getproducts', views.get_products),
    path('getproduct/<int:product_id>', views.get_product),

    path('getusers', views.get_users),
    path('getuser/<int:user_id>', views.get_user),

    path('addproduct', views.add_product),
    path('adduser', views.add_user),

    path('updateproduct/<int:product_id>', views.update_product),
    path('updateuser/<int:user_id>', views.update_user),

    path('deleteproduct/<int:product_id>', views.delete_product),
    path('deleteuser/<int:user_id>', views.delete_user)
]

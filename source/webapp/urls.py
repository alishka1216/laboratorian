from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='product-list'),
    path('product/add/', product_create_view, name='product-add'),
    path('product/update/<int:pk>/', product_update_view, name='product-update'),
    path('product/delete/<int:pk>/', product_delete_view, name='product-delete')
]
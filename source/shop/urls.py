from django.contrib import admin
from django.urls import path
from webapp.views import (
    index_view,
    product_view,
    product_create_view,
    product_update_view,
    product_delete_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='product-list'),
    path('product/<int:pk>/', product_view, name='product-view'),
    path('product/add/', product_create_view, name='product-add'),
    path('product/update/<int:pk>/', product_update_view, name='product-update'),
    path('product/delete/<int:pk>/', product_delete_view, name='product-delete')
]
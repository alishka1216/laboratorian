from django.contrib import admin
from django.urls import path
from webapp.views import (
    IndexView,
    ProductView,
    ProductUpdateView,
    ProductDeleteView,
    ProductCreateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductView.as_view(), name='product-view'),
    path('product/add/', ProductCreateView.as_view(), name='product-add'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete')
]
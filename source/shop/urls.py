from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.urls import path
from webapp.views import (
    IndexView,
    ProductView,
    ProductUpdateView,
    ProductDeleteView,
    ProductCreateView,
    BasketListView,
    BasketView,
    BasketDeleteBack,
    OrderCreateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductView.as_view(), name='product-view'),
    path('product/add/', ProductCreateView.as_view(), name='product-add'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    path('product/basket/', BasketListView.as_view(), name='basket-view'),
    path('product/send/<int:pk>/', BasketView.as_view(), name='basket-send'),
    path('product/basket/delete/<int:pk>/', BasketDeleteBack.as_view(), name='basket-delete'),
    path('order/', OrderCreateView.as_view(), name='order-add'),
    path('accounts/', include('accounts.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
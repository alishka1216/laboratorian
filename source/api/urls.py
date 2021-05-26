from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ProductViewSet, OrderViewSet, ProductOrderViewSet

app_name = 'api'

api_router = DefaultRouter()
api_router.register('products', ProductViewSet),
api_router.register('orders', OrderViewSet),
api_router.register('productOrder', ProductOrderViewSet)


urlpatterns = [
    path('', include(api_router.urls))
]
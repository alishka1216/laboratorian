from webapp.models import Order
from api.serializers import OrderSerializer
from rest_framework.viewsets import ModelViewSet


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
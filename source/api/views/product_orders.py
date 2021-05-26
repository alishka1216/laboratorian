from rest_framework import status
from rest_framework.response import Response

from webapp.models import Product_order, Order
from api.serializers import ProductOrderSerializer, OrderSerializer
from rest_framework.viewsets import ModelViewSet


class ProductOrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    # def perform_create(self, serializer):
    #     return serializer.save()
    #
    # def create(self, request, *args, **kwargs):
    #     ser = self.get_serializer(data=request.data)
    #     if ser.is_valid(raise_exception=True):
    #         data = self.perform_create(ser)
    #         print(ser.data)
    #         print(data)
    #         return Response(data=data, status=status.HTTP_201_CREATED)



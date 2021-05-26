from rest_framework import serializers
from webapp.models import Product, Order, Product_order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description', 'category', 'reminder', 'price')


class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_order
        fields = ('product', 'total')


class OrderSerializer(serializers.ModelSerializer):
    order_products = ProductOrderSerializer(many=True, read_only=False)

    class Meta:
        model = Order
        fields = ('order_products', 'name', 'number', 'adress')

    def create(self, validated_data):
        order = Order.objects.create(name=validated_data['name'], adress=validated_data['adress'], number=validated_data['number'])
        for i in validated_data['order_products']:
            p = Product_order.objects.create(order=order, product=i['product'], total=i['total'])
            print(p)
        return validated_data

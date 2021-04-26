from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from webapp.models import Basket, Order, Product_order
from django.views.generic import CreateView, ListView
from webapp.forms import OrderForm
from django.shortcuts import render, get_object_or_404


class OrderCreateView(CreateView):
    template_name = 'basket/basket_list.html'
    model = Order
    # model = get_user_model()
    form_class = OrderForm
    permission_required = 'webapp.add_order'

    def form_valid(self, form):
        order = form.save()
        if self.request.user.is_authenticated:
            order.user = self.request.user
        order.save()
        for i in Basket.objects.all():
            Product_order.objects.create(product=i.product, order=order, total=i.total)
            i.delete()
        return redirect('product-list')


class OrderListView(ListView):
    template_name = 'order/order_list.html'
    model = Product_order
    context_object_name = 'orders'
    def get_queryset(self):
        return Product_order.objects.filter(order__user_id=self.request.user.pk)

    def get_context_data(self, *, object_list=None, **kwargs):
        total = 0
        for i in self.object_list:
            total += i.total * i.product.price
        context = super(OrderListView, self).get_context_data(object_list=object_list)
        context['total'] = total

        return context

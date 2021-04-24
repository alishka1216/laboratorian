from django.shortcuts import redirect
from webapp.models import Basket, Order, Product_order
from django.views.generic import CreateView
from webapp.forms import OrderForm



class OrderCreateView(CreateView):
    template_name = 'basket/basket_list.html'
    model = Order
    form_class = OrderForm
    permission_required = 'webapp.add_order'

    def form_valid(self, form):
        order = form.save()
        for i in Basket.objects.all():
            Product_order.objects.create(product=i.product, order=order, total=i.total)
            i.delete()
        return redirect('product-list')
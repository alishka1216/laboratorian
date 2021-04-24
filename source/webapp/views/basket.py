from django.shortcuts import get_object_or_404, redirect
from webapp.models import Product, Basket
from django.views.generic import ListView, DeleteView, View
from django.urls import reverse_lazy
from webapp.forms import OrderForm



class BasketListView(ListView):
    template_name = 'basket/basket_list.html'
    model = Basket
    context_object_name = 'baskets'
    paginate_by = 10
    paginate_orphans = 3

    def get_queryset(self):
        cart = self.request.session.get('cart', [])
        print(cart)
        return Basket.objects.filter(pk__in=cart)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['form'] = OrderForm()
        return context


class BasketView(View):
    def get(self, request, *args, **kwargs):
        session = request.session.get('cart', [])
        print(session)
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        if product.reminder > 0:
            try:
                basket = Basket.objects.get(product__pk=product.pk, pk__in=session)
                basket.total += 1
                basket.save()
            except Basket.DoesNotExist:
                b = Basket.objects.create(product=product, total=1)
                print(b)
                session.append(b.pk)
            request.session['cart'] = session
            print(request.session['cart'])
            product.reminder -= 1
            product.save()
        else:
            pass
        return redirect('product-list')


class BasketDeleteBack(DeleteView):
    template_name = 'basket/basket_delete.html'
    model = Basket
    context_object_name = 'basket'
    success_url = reverse_lazy('product-list')
    permission_required = 'webapp.delete_basket'

    def post(self, request, *args, **kwargs):
        session = request.session.get('cart', [])
        basket = self.get_object()
        product = basket.product
        product.reminder += basket.total
        session.remove(basket.pk)
        request.session['cart'] = session
        product.save()

        return super(BasketDeleteBack, self).post(request, *args, *kwargs)








# def get_queryset(self):
#     queryset = super().get_queryset()
#     if self.search_value:
#         query = Q(product__icontains=self.search_value) | Q(description__icontains=self.search_value)
#         queryset = queryset.filter(query)
#     return queryset.order_by('product', 'categories').exclude(remainder=0)

# def get(self, request, *args, **kwargs):
#     self.form = self.get_search_form()
#     self.search_value = self.get_search_value()
#     return super().get(request, *args, **kwargs)
#
#
# def get_search_form(self):
#     return SearchForm(self.request.GET)
#
#
# def get_search_value(self):
#     if self.form.is_valid():
#         return self.form.cleaned_data['search']
#     return None
#
#
# def get_context_data(self, *, object_list=None, **kwargs):
#     context = super().get_context_data(object_list=object_list, **kwargs)
#     context['form'] = self.form
#     context['search'] = self.search_value
#     if self.search_value:
#         context['query'] = urlencode({'search': self.search_value})
#     return context

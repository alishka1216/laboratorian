from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product, Basket, Order, Product_order
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View, TemplateView, RedirectView, FormView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from webapp.forms import ProductFrom, SearchForm, OrderForm
from django.db.models import Q
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


def get(self, request, *args, **kwargs):
    self.form = self.get_search_form()
    self.search_value = self.get_search_value()
    return super().get(request, *args, **kwargs)


def get_search_form(self):
    return SearchForm(self.request.GET)


def get_search_value(self):
    if self.form.is_valid():
        return self.form.cleaned_data['search']
    return None


def get_context_data(self, *, object_list=None, **kwargs):
    context = super().get_context_data(object_list=object_list, **kwargs)
    context['form'] = self.form
    context['search'] = self.search_value
    if self.search_value:
        context['query'] = urlencode({'search': self.search_value})
    return context


def get_queryset(self):
    queryset = super().get_queryset()
    if self.search_value:
        query = Q(product__icontains=self.search_value) | Q(description__icontains=self.search_value)
        queryset = queryset.filter(query)
    return queryset.order_by('product', 'categories').exclude(remainder=0)


# Create your views here.

class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 10
    paginate_orphans = 3



class ProductView(DetailView):
    template_name = 'product_view.html'
    model = Product
    context_object_name = 'product'


class ProductCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'product_create.html'
    model = Product
    form_class = ProductFrom
    permission_required = 'webapp.add_product'

    def get_success_url(self):
        return reverse('product-view', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin,UpdateView):
    model = Product
    template_name = 'product_update.html'
    form_class = ProductFrom
    context_object_name = 'product'
    permission_required = 'webapp.change_product'

    def get_success_url(self):
        return reverse('product-view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'product_delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('product-list')
    permission_required = 'webapp.delete_product'


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
        basket = self.get_object()
        product = basket.product
        product.reminder += basket.total
        product.save()
        return super(BasketDeleteBack, self).post(request, *args, *kwargs)


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

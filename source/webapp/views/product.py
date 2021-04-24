from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product, Basket, Order, Product_order
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View, TemplateView, RedirectView, FormView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from webapp.forms import ProductFrom, SearchForm, OrderForm
from django.db.models import Q
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


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
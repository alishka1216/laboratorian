from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product, category_choices
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View, TemplateView, RedirectView, FormView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from webapp.forms import ProductFrom


# Create your views here.

class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'product'
    paginate_by = 10
    paginate_orphans = 3


class ProductView(DetailView):
    template_name = 'product_view.html'
    model = Product
    context_object_name = 'product'


class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    model = Product
    form_class = ProductFrom

    def get_success_url(self):
        return reverse('product-view', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_update.html'
    form_class = ProductFrom
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product-view', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'product_delete.html'
    model = Product
    context_object_name = 'product'

    success_url = reverse_lazy('product-list')
